import networkx as nx
import pandas as pd
import os

def build_graph(data):
    """Builds a directed transaction graph."""
    G = nx.DiGraph()
    for _, row in data.iterrows():
        G.add_edge(row['sender'], row['receiver'], amount=row['amount'], time=row['time'])
    return G

def add_transaction_weights(G, data):
    """Adds weights to graph edges based on transaction amount."""
    for _, row in data.iterrows():
        if G.has_edge(row['sender'], row['receiver']):
            G[row['sender']][row['receiver']]['weight'] += row['amount']
        else:
            G.add_edge(row['sender'], row['receiver'], weight=row['amount'])
    return G

if __name__ == "__main__":
    input_file = "data/processed/cleaned_transactions.csv"
    output_file = "data/processed/transaction_graph.gexf"

    # Validate input file
    if not os.path.exists(input_file):
        raise FileNotFoundError(f"Input file '{input_file}' does not exist.")

    # Load data and build graph
    data = pd.read_csv(input_file)
    G = build_graph(data)
    G = add_transaction_weights(G, data)

    # Ensure output directory exists
    os.makedirs(os.path.dirname(output_file), exist_ok=True)
    
    # Save graph to file
    nx.write_gexf(G, output_file)
    print(f"Transaction graph saved to {output_file}.")
