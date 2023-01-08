# ----------------------------------------------------------------------
# QASMBench: A Low-level OpenQASM Benchmark Suite
# ----------------------------------------------------------------------
# Samuel Stein, Ang Li
# Pacific Northwest National Laboratory(PNNL), U.S.
# BSD Lincese.
# Created 05/01/2023.
# PNNL IPID: 31924-E, IR: PNNL-SA-153380, PNNL-SA-162867, ECCN:EAR99
# ----------------------------------------------------------------------


from typing import *
import numpy as np
import matplotlib.pyplot as plt
import glob
import qiskit
import os
from metrics.QMetric import QMetric


class MetricPlotter:
    """
    MetricPlotter is an object responsible for generating plots similar to that in QASMBench on a group of metrics.
    QASMBench paper link : https://arxiv.org/pdf/2005.13018.pdf
    SupermarQ paper link: https://arxiv.org/abs/2202.11045
    Support for QASMBENCH metrics and SupermarQ are implemented. Custom metric lists can be implemented, provided
    they are implemented under the QMetric.py file as well. For usage of the metrics, they should exist alongside the
    object (e.g. QMetric.CUSTOMMETRIC = float ).

    """

    def __init__(self, custom_keys: list[str] = None, file_path: str = "."):
        self.QASMBENCH_KEYS: list[str] = ["circuit_depth", "circuit_width", "retention_lifespan",
                                          "gate_density", "measurement_density", "entanglement_variance"]
        self.SUPERMARQ_KEYS: list[str] = ["communication_supermarq", "measurement_supermarq", "depth_supermarq",
                                          "parallelism_supermarq", "entanglement_supermarq", "liveness_supermarq"]
        self.CUSTOM_KEYS: list[str] = custom_keys
        self.PROCESSED_FEATURES = {"SMALL": [],
                                   "MEDIUM": [],
                                   "LARGE": []}
        self.CIRCUIT_SIZES = {"SMALL": 10,
                              "MEDIUM": 28,
                              "LARGE": 433}
        self.SIZE_KEYS = ["SMALL", "MEDIUM", "LARGE"]
        self.file_path = file_path
        self.files = []

    @staticmethod
    def evaluate_qasm(qasm: str) -> Dict:
        """
        Evaluates a qasm string according to QMetric
        :param qasm: QASM string representing circuit that is to be evaluated
        :return: Dictionary containing information regarding each feature in QMetric
        """
        return QMetric(qasm).evaluate_qasm()

    def search_for_qasm(self) -> None:
        """
        Function to search file_path for all QASM files under the directory. Each QASM file will be added
        to the file list.
        :return: None
        """
        for root, dirs, files in os.walk(self.file_path):
            for file in files:
                if file.endswith(".qasm"):
                    self.files.append(os.path.join(root, file))

    def load_next_qasm_to_circuit(self) -> qiskit.QuantumCircuit:
        """
        Iterator object over each circuit in the self.files, populated via self.search_for_qasm().
        :return: Returns a quantum circuit representing the next circuit in the list.
        """
        assert len(self.files) > 0
        for file in self.files:
            circuit = qiskit.QuantumCircuit().from_qasm_file(file)
            yield circuit

    def load_next_qasm(self) -> str:
        """
        Iterator object over each QASM in the self.files, populated via self.search_for_qasm().
        :return: Returns a QASM string representing the next circuit in the list.
        """
        assert len(self.files) > 0
        for file in self.files:
            with open(file, 'r') as f:
                try:
                    qasm = f.read()
                except:
                    print(f"{file} failed to evaluate - Problem with loading QASM. Skipping to next.")
                    continue
            circuit_name = file.split('/')[-1].rstrip('qasm.')
            yield qasm, circuit_name

    def process_qasm_files(self) -> None:
        """
        Iterate over each QASM file in the self.files object, and process each using the QMetric file.
        Each processed file will populate a result in the self.PROCESSED_FEATURES dictionary, with the
        tag of the file name.
        """
        qasm_files = self.load_next_qasm()
        for qasm, circuit_name in qasm_files:
            feature_dict = QMetric(qasm).evaluate_qasm()
            if feature_dict['qubit_count'] <= self.CIRCUIT_SIZES["SMALL"]:
                self.PROCESSED_FEATURES["SMALL"].append({circuit_name: feature_dict})
            elif feature_dict['qubit_count'] <= self.CIRCUIT_SIZES["MEDIUM"]:
                self.PROCESSED_FEATURES["MEDIUM"].append({circuit_name: feature_dict})
            else:
                self.PROCESSED_FEATURES["LARGE"].append({circuit_name: feature_dict})

    @staticmethod
    def format_circuit_name(circ, seperator="_"):
        """
        :param circ: String title of a circuit such as "GHZ-State" or "QFT-Large-Circuit-n48"
        :param seperator: The separator used in the file naming. For QASMBench this is "_"
        :return: Returns a tidied circuit title for plotting. Will transform "qft_large_n48" into "Qft Large N48"
        """
        edited_circuit_name = circ.replace(seperator, " ")
        edited_circuit_name = edited_circuit_name.title()
        return edited_circuit_name

    @staticmethod
    def format_feature_name(feature, seperator="_"):
        """
        :param circ: String title of a circuit such as "GHZ-State" or "QFT-Large-Circuit-n48"
        :param seperator: The separator used in the file naming. For QASMBench this is "_"
        :return: Returns a tidied circuit title for plotting. Will transform "qft_large_n48" into "Qft Large N48"
        """
        edited_feature_name = feature.replace(seperator, " ")
        edited_feature_name = edited_feature_name.title()
        return edited_feature_name

    def max_of_feature(self, feature):
        """
        :param feature: Feature to search for the largest value over.
        :return: Return the highest value from the search.
        """
        peak = -1
        for key in self.SIZE_KEYS:
            for circuit in self.PROCESSED_FEATURES[key]:
                circuit_name = list(circuit.keys())[0]
                if circuit[circuit_name][feature] > peak:
                    peak = circuit[circuit_name][feature]
        return peak

    def plot_feature(self, feature, figsize=None,
                     bar_width=1,
                     plot_limit=None,
                     scale_factor=1.1,
                     filepath=None,
                     color_palette=plt.cm.tab20c.colors):
        """
        :param feature: The target feature to be plotted. Must exist under the self.PROCESSED_FEATURES tag.
        :param figsize: Figure size to be set before plotting. If left as None, it will default to 10,20
        :param bar_width: Width of the bar being plotted
        :param plot_limit: Limit of the plot. If left as None, the limit will be set to SCALE_FACTOR times the max value
        :param scale_factor: The factor to multiply the plot_limit value to. For example, Plot_limit of 2 and Scale
        factor of 1.5 will result in a ylimit of 3
        :param filepath: File path to save the plot to. Will save as a pdf.
        :param color_palette: Color palette to be used for the plot. Default is the tab20c color palette. Ensure color
        palette is iterable.
        :return: None
        """
        plt.clf()
        if figsize is None:
            plt.figure(figsize=(10, 20))
        else:
            plt.figure(figsize=figsize)
        if plot_limit is None:
            plot_limit = scale_factor * self.max_of_feature(feature)
        pos = 0.5 * bar_width
        circuit_pos = []
        circuit_names = []
        vline_position = [0]
        clr_index = 0
        for key in self.SIZE_KEYS:
            has_size = False
            for result in self.PROCESSED_FEATURES[key]:
                has_size = True
                circuit_name = list(result.keys())[0]
                plt.bar(pos, result[circuit_name][feature], width=bar_width, color=color_palette[clr_index])
                clr_index += 1
                if clr_index >= len(color_palette):
                    clr_index = 0
                circuit_pos.append(pos)
                circuit_names.append(self.format_circuit_name(circuit_name))
                pos += bar_width
            if key != "LARGE" and has_size:
                plt.vlines(pos, 0, plot_limit, linewidth=2, color='black')
                vline_position.append(pos)
                pos += bar_width
                plt.text(x=-0.5 * bar_width + (vline_position[-2] + vline_position[-1]) / 2,
                         y=0.9 * plot_limit, s=key, fontweight="bold")
            elif key == "LARGE" and has_size:
                vline_position.append(pos)
                plt.text(x=-0.5 * bar_width + (vline_position[-2] + vline_position[-1]) / 2,
                         y=0.9 * plot_limit, s=key, fontweight="bold")
        plt.xticks(circuit_pos, circuit_names, rotation=90)
        plt.ylim(0, plot_limit)
        plt.xlim(0, circuit_pos[-1] + 0.5 * bar_width)
        plt.grid(axis='y')
        plt.ylabel(self.format_feature_name(feature))
        if filepath is not None:
            plt.savefig(filepath)
