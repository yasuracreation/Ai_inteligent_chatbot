from intalentasia.infrastructure.config.settings import get_settings
from intalentasia.infrastructure.config.logging import configure_logging
class Container:
    def __init__(self) -> None:
        self.settings = get_settings()  
        configure_logging()  

       
        self.vector_store = None          
        self.orchestrator = None          
        self.auth_repository = None       
        self.chat_use_case = None         
        self.stream_chat_use_case = None  


def create_container() -> Container:
    return Container()