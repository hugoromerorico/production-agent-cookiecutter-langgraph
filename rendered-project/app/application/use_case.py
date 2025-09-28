from app.application.workflows.wf1.graph import get_graph

class UseCase:
    """Defines an application use case,
     coordinating entities and services to implement business workflows
      as per clean architecture principles."""

    def __init__(self):
        self.graph = get_graph()
        pass

    def execute(self):
        result = self.graph.invoke({})
        return result
