import streamlit as st
from llm import llm
from graph import graph

from langchain_neo4j import GraphCypherQAChain

cypher_qa = GraphCypherQAChain.from_llm(
    llm,
    graph=graph,
    verbose=True,
    allow_dangerous_requests=True
)