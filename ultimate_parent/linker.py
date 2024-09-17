class Linker:
    def __init__(self, relation: tuple[str, str]) -> None:
        self.min_child_item = relation[0]
        self.max_parent_item = relation[1]
        self.relations = [relation]

    def _check_min_child_item(self, relation: tuple) -> bool:
        if self.min_child_item == relation[1]:
            self.min_child_item = relation[0]
            self.relations.append(relation)
            return True
        return False

    def _check_max_parent_item(self, relation: tuple) -> bool:
        if self.max_parent_item == relation[0]:
            self.max_parent_item = relation[1]
            self.relations.append(relation)
            return True
        return False

    def _check_min_linker_child_item(self, linker: "Linker") -> bool:
        if self.min_child_item == linker.max_parent_item:
            self.min_child_item = linker.min_child_item
            self.relations + linker.relations
            return True
        return False

    def _check_max_linker_child_item(self, linker: "Linker") -> bool:
        if self.max_parent_item == linker.min_child_item:
            self.max_parent_item = linker.max_parent_item
            self.relations + linker.relations
            return True
        return False

linker_list: list[Linker] = []

i = 0
for relation in relations:
    for linker in linker_list:
        if any(
            [
                linker._check_max_parent_item(relation),
                linker._check_min_child_item(relation),
            ]
        ):
            continue
        else:
            linker_list.append(Linker(relation=relation))

# everything is now either a linker or added to a linker
while True:
    linked = 0
    for index in range(len(linker_list)):
        base_linker = linker_list[index]
        for linker in [linker_list[:index] + linker_list[index + 1 :]]:
            if any(
                [
                    base_linker._check_min_linker_child_item(linker),
                    base_linker._check_max_linker_child_item(linker),
                ]
            ):
                linked += 1
    if linked == 0:
        break
