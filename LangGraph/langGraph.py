import networkx as nx
from transformers import pipeline
import LangGraph
G = nx.DiGraph()

G.add_node("Finanzauto", description="Empresa colombiana que ofrece servicios financieros para la compra de vehículos.")
G.add_node("Crédito Vehicular", description="Finanzauto ofrece créditos para la financiación de autos nuevos y usados.")
G.add_node("Leasing Vehicular", description="Opción de leasing ofrecida por Finanzauto, donde los clientes pueden utilizar un vehículo con opción de compra al final.")
G.add_node("Seguros Vehiculares", description="Finanzauto ofrece seguros para autos nuevos y usados.")
G.add_node("Solicitud de Crédito", description="Proceso para solicitar un crédito en Finanzauto a través de la página web.")
G.add_node("Refinanciación", description="Finanzauto permite a los clientes refinanciar vehículos y mejorar sus condiciones de deuda.")
G.add_node("Política de Calidad", description="Estamos certificados por Bureau Veritas en Colocación y Cobro de Cartera para Crédito de Vehículos.")
G.add_node("Derechos Humanos", description="Finanzauto esta comprometida con el respeto hacia los Derechos Humanos, razón por la cual rechazamos cualquier acción que contribuya a la afectación de los mismos. Adicionalmente, reconocemos la importancia de que los trabajadores conozcan, comprendan y ejerzan sus actividades diarias implementando el respeto y el valor que los Derechos Humanos requieren.")
G.add_node("Prevencón del Acoso Laboral", description="Establecemos mecanismos de prevención de las conductas de acoso laboral, dando cumplimiento a la normatividad nacional vigente.")
G.add_node("Seguridad y Salud en el Trabajo", description="Finanzauto esta comprometida con la implementación del Sistema de Gestión de Seguridad y Salud en el Trabajo, dando cumplimiento la legislación nacional vigente aplicable en materia de riesgos laborales y demás requisitos que haya suscrito la Compañía.")
G.add_node("Protección de Datos Personales", description="De acuerdo a lo previsto en la Ley 1581 de 2012 y el Decreto 1074 de 2015, así como toda la normatividad vigente, hemos implementado la Política del Sistema Integral de Protección de Datos Personales.")
G.add_node("Seguridad de la información", description="Garantizamos la confidencialidad, integridad y disponibilidad de la información, asegurando que los trabajadores sigan prácticas seguras y coherentes en el uso y manejo de los datos.")



G.add_edge("Finanzauto", "Crédito Vehicular", relationship="ofrece")
G.add_edge("Finanzauto", "Leasing Vehicular", relationship="ofrece")
G.add_edge("Finanzauto", "Seguros Vehiculares", relationship="ofrece")
G.add_edge("Finanzauto", "Solicitud de Crédito", relationship="facilita")
G.add_edge("Finanzauto", "Refinanciación", relationship="ofrece")
G.add_edge("Finanzauto", "Política de Calidad", relationship="ofrece")
G.add_edge("Finanzauto", "Derechos Humanos", relationship="ofrece")
G.add_edge("Finanzauto", "Prevencón del Acoso Laboral", relationship="ofrece")
G.add_edge("Finanzauto", "Seguridad y Salud en el Trabajo", relationship="ofrece")
G.add_edge("Finanzauto", "Protección de Datos Personales", relationship="ofrece")
G.add_edge("Finanzauto", "Seguridad de la información", relationship="ofrece")

lg = LangGraph(graph=G, model_name="gpt2")

generator = pipeline("text-generation", model="gpt2")

def query_langgraph_system(question):
    subgraph = lg.query(question)
    
    context = " ".join([node['description'] for node in subgraph['nodes']])
    response = generator(question + " " + context, max_length=100, num_return_sequences=1)
    return response[0]['generated_text']

if __name__ == "__main__":
    while True:
        question = input("Haz una pregunta: ")
        if question.lower() == "salir":
            break
        response = query_langgraph_system(question)
        print(f"Respuesta: {response}")
