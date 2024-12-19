import networkx as nx
import pandas as pd

def build_graph(data):
    """Builds a transaction graph."""
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
    data = pd.read_csv("data/processed/cleaned_transactions.csv")
    G = build_graph(data)
    G = add_transaction_weights(G, data)
    nx.write_gexf(G, "data/processed/transaction_graph.gexf")
