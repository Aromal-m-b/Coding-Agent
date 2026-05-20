from typing import TypedDict

class AgentState(TypedDict):
    messages:list[str]
    intent:str
    complexity:str
    test_status:str
    agent_stat:str

def Supervisor_Node(state:AgentState):
    if state["intent"] == None:
        print("Starting Coding Agent")
        state["intent"] = "test"
    else:
        print("Coding Agent Running ")

    return state

state = {
    "messages":[],
    "intent":None,
    "complexity":None,
    "test_status":None,
    "agent_stat":None
}
state = Supervisor_Node(state)
Supervisor_Node(state)
print(state)