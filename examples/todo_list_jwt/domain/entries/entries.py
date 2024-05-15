class Entry:
    id: int
    text: str


class ListState(State):
    entries: list[Entry] = []


class EntriesViewModel:
    def __init__(self) -> None:
        self.state = ListState()

    def add(self, entry: str) -> ListState:
        self.state.entries.append({"text": entry, "id": len(self._list)})
        return self.state

    def remove(self, entry_id: int) -> ListState:
        self.state.entries = [x for x in self._list if x.id != entry_id]
        return self.state
