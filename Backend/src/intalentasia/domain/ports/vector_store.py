from typing import List, Protocol

from intalentasia.domain.entities.document_chunk import DocumentChunk
from intalentasia.domain.value_objects.search_query import SearchQuery


class IVectorStoreRepository(Protocol):
    def hybrid_search(self, query: SearchQuery) -> List[DocumentChunk]:
        ...

    def upsert_chunks(self, chunks: List[DocumentChunk]) -> None:
        ...
