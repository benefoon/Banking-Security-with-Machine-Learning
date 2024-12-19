import streamlit as st
import pandas as pd
import networkx as nx
from pyvis.network import Network

def visualize_graph(file_path):
    """Visualizes the transaction graph."""
    G = nx.read_gexf(file_path)
    net = Network(notebook=True)
    net.from_nx(G)
    return net

st.title("Suspicious Money Flow Dashboard")

uploaded_file = st.file_uploader("Upload Graph File", type="gexf")
if uploaded_file:
    net = visualize_graph(uploaded_file)
    net.show("graph.html")
    st.components.v1.html(open("graph.html", "r").read(), height=600)
