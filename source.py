import time

class Node:
    def __init__(self, value):
        self.value = value
        self.children = []  # Liste des enfants

class BinaryNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None

    def display_breadth_first(self):
        if not self.root:
            return
        queue = [self.root]
        while queue:
            current = queue.pop(0)
            print(current.value, end=' ')
            if current.left:
                queue.append(current.left)
            if current.right:
                queue.append(current.right)
        print()

class NaryTree:
    def __init__(self):
        self.root = None

    # Construction d'un arbre n-aire (aléatoire, comme avant)
    def construct_tree(self, values):
        if not values:
            return None
        self.root = Node(values[0])
        queue = [self.root]
        index = 1
        while index < len(values):
            current = queue.pop(0)
            for _ in range(4):  # maximum 4 enfants
                if index < len(values):
                    child = Node(values[index])
                    current.children.append(child)
                    queue.append(child)
                    index += 1
                else:
                    break

    # Construction d'un arbre complet (nouveau)
    def construct_complete_tree(self):
        # Arbre 4-aire complet : hauteur 3, 21 nœuds
        values = [f'F{i}' for i in range(21)]
        self.root = Node(values[0])  # Racine
        queue = [self.root]
        index = 1
        level = 0
        nodes_per_level = [1, 4, 16]  # Nombre de nœuds par niveau pour hauteur 3
        while index < len(values) and level < len(nodes_per_level):
            current_level_nodes = []
            for _ in range(nodes_per_level[level]):
                if queue:
                    current = queue.pop(0)
                    current_level_nodes.append(current)
            for node in current_level_nodes:
                for _ in range(4):  # Exactement 4 enfants par nœud interne
                    if index < len(values):
                        child = Node(values[index])
                        node.children.append(child)
                        queue.append(child)
                        index += 1
            level += 1

    # Affichage de l'arbre en largeur
    def display_breadth_first(self):
        if not self.root:
            return
        queue = [self.root]
        while queue:
            current = queue.pop(0)
            print(current.value, end=' ')
            for child in current.children:
                queue.append(child)
        print()

    # Affichage de l'arbre en profondeur
    def display_depth_first(self, node):
        if node:
            print(node.value, end=' ')
            for child in node.children:
                self.display_depth_first(child)

    # Calculer la hauteur de l'arbre
    def height(self, node):
        if not node:
            return 0
        if not node.children:
            return 1
        heights = [self.height(child) for child in node.children]
        return 1 + max(heights)

    # Recherche d'une information
    def search(self, node, value):
        if not node:
            return None
        if node.value == value:
            return node
        for child in node.children:
            found = self.search(child, value)
            if found:
                return found
        return None

    # Insérer un nœud
    def insert(self, parent_value, new_value):
        parent_node = self.search(self.root, parent_value)
        if parent_node and len(parent_node.children) < 4:
            parent_node.children.append(Node(new_value))

    # Modifier un nœud
    def modify_node(self, old_value, new_value):
        node = self.search(self.root, old_value)
        if node:
            node.value = new_value

    # Supprimer un nœud
    def delete_node(self, value):
        parent_node = self.find_parent(self.root, value)
        if parent_node:
            parent_node.children = [child for child in parent_node.children if child.value != value]

    def find_parent(self, node, value):
        if not node:
            return None
        for child in node.children:
            if child.value == value:
                return node
            parent = self.find_parent(child, value)
            if parent:
                return parent
        return None

    # Vérifier si l'arbre est complet (corrigé)
    def is_complete(self):
        if not self.root:
            return True
        h = self.height(self.root)
        return self._is_complete(self.root, 0, h - 1)

    def _is_complete(self, node, level, max_level):
        if not node:
            return True
        # Si on est au dernier niveau, le nœud doit être une feuille (pas d'enfants)
        if level == max_level:
            return len(node.children) == 0
        # Sinon, le nœud doit avoir exactement 4 enfants
        if len(node.children) != 4:
            return False
        # Vérifier récursivement pour tous les enfants
        for child in node.children:
            if not self._is_complete(child, level + 1, max_level):
                return False
        return True

    # Trouver un sous-arbre complet maximal
    def find_max_complete_subtree(self):
        return self._find_max_complete_subtree(self.root)

    def _find_max_complete_subtree(self, node):
        if not node:
            return None
        if len(node.children) == 4:
            return node
        for child in node.children:
            result = self._find_max_complete_subtree(child)
            if result:
                return result
        return None

    # Extraire un sous-arbre
    def extract_subtree(self, value):
        node = self.search(self.root, value)
        if node:
            new_tree = NaryTree()
            new_tree.root = node
            return new_tree
        return None

    # Transformer en arbre binaire
    def to_binary_tree(self):
        if not self.root:
            return None
        def convert(node):
            if not node:
                return None
            bin_node = BinaryNode(node.value)
            if node.children:
                bin_node.left = convert(node.children[0])  # Premier enfant comme fils gauche
                current = bin_node.left
                for child in node.children[1:]:  # Les autres comme frères droits
                    current.right = convert(child)
                    current = current.right
            return bin_node
        bin_tree = BinaryTree()
        bin_tree.root = convert(self.root)
        return bin_tree

# Fonctions de construction d'arbres (aléatoires, comme avant)
def constArbre10():
    return construct_tree_with_values(10)

def constArbre20():
    return construct_tree_with_values(20)

def constArbre30():
    return construct_tree_with_values(30)

def constArbre40():
    return construct_tree_with_values(40)

def constArbre50():
    return construct_tree_with_values(50)

def constArbre100():
    return construct_tree_with_values(100)

def construct_tree_with_values(n):
    values = [f'F{i}' for i in range(n)]
    tree = NaryTree()
    tree.construct_tree(values)
    return tree

# Menu de démarrage (mis à jour)
def main():
    tree = NaryTree()

    while True:
        print("\nMenu:")
        print("1. Construire un arbre (4-aire aléatoire)")
        print("2. Construire un arbre (4-aire complet)")
        print("3. Afficher l'arbre (Largeur)")
        print("4. Afficher l'arbre (Profondeur)")
        print("5. Calculer la hauteur de l'arbre")
        print("6. Rechercher une information")
        print("7. Insérer un nœud")
        print("8. Modifier un nœud")
        print("9. Supprimer un nœud")
        print("10. Afficher un sous-arbre")
        print("11. Vérifier si l'arbre est complet")
        print("12. Trouver un sous-arbre complet maximal")
        print("13. Extraire un sous-arbre")
        print("14. Transformer en arbre binaire")
        print("15. Quitter")

        choice = int(input("Choisissez une option: "))
        if choice == 1:
            print("Choisissez le nombre de nœuds:")
            print("1. 10 nœuds")
            print("2. 20 nœuds")
            print("3. 30 nœuds")
            print("4. 40 nœuds")
            print("5. 50 nœuds")
            print("6. 100 nœuds")

            node_choice = int(input("Entrez votre choix: "))
            if node_choice == 1:
                tree = constArbre10()
            elif node_choice == 2:
                tree = constArbre20()
            elif node_choice == 3:
                tree = constArbre30()
            elif node_choice == 4:
                tree = constArbre40()
            elif node_choice == 5:
                tree = constArbre50()
            elif node_choice == 6:
                tree = constArbre100()
            else:
                print("Choix invalide.")
            # Affichage automatique après construction
            print("Arbre construit (aléatoire) :")
            tree.display_breadth_first()

        elif choice == 2:
            tree = NaryTree()
            tree.construct_complete_tree()
            # Affichage automatique après construction
            print("Arbre construit (complet, 21 nœuds, hauteur 3) :")
            tree.display_breadth_first()

        elif choice == 3:
            tree.display_breadth_first()
        elif choice == 4:
            print("Affichage en profondeur:")
            tree.display_depth_first(tree.root)
            print()
        elif choice == 5:
            height = tree.height(tree.root)
            print(f"Hauteur de l'arbre: {height}")
        elif choice == 6:
            value = input("Entrez la valeur à rechercher: ")
            node = tree.search(tree.root, value)
            if node:
                print(f"Nœud trouvé: {node.value}")
            else:
                print("Nœud non trouvé.")
        elif choice == 7:
            parent_value = input("Entrez la valeur du parent: ")
            new_value = input("Entrez la valeur du nouveau nœud: ")
            tree.insert(parent_value, new_value)
            # Affichage automatique après insertion
            print("Arbre après insertion :")
            tree.display_breadth_first()
        elif choice == 8:
            old_value = input("Entrez la valeur du nœud à modifier: ")
            new_value = input("Entrez la nouvelle valeur: ")
            tree.modify_node(old_value, new_value)
            # Affichage automatique après modification
            print("Arbre après modification :")
            tree.display_breadth_first()
        elif choice == 9:
            value = input("Entrez la valeur du nœud à supprimer: ")
            tree.delete_node(value)
            # Affichage automatique après suppression
            print("Arbre après suppression :")
            tree.display_breadth_first()
        elif choice == 10:
            value = input("Entrez la valeur du nœud dont vous voulez afficher le sous-arbre: ")
            subtree = tree.extract_subtree(value)
            if subtree:
                print(f"Sous-arbre de {subtree.root.value}:")
                subtree.display_breadth_first()
            else:
                print("Sous-arbre non trouvé.")
        elif choice == 11:
            start_time = time.perf_counter()  # Changé pour plus de précision
            if tree.is_complete():
                print("L'arbre est complet.")
            else:
                print("L'arbre n'est pas complet.")
            end_time = time.perf_counter()
            execution_time_ns = (end_time - start_time) * 1e9  # Temps en nanosecondes
            # Fonction pour afficher le temps de manière significative
            if execution_time_ns >= 1e6:  # ≥ 1 ms
                execution_time_ms = execution_time_ns / 1e6
                print(f"Le temps d'exécution est de {execution_time_ms:.4f} ms.")
            elif execution_time_ns >= 1e3:  # ≥ 1 µs
                execution_time_us = execution_time_ns / 1e3
                print(f"Le temps d'exécution est de {execution_time_us:.2f} µs.")
            else:  # < 1 µs
                print(f"Le temps d'exécution est de {execution_time_ns:.0f} ns.")
        elif choice == 12:
            start_time = time.perf_counter()  # Changé pour plus de précision
            subtree = tree.find_max_complete_subtree()
            if subtree:
                print(f"Sous-arbre complet maximal trouvé: {subtree.value}")
            else:
                print("Aucun sous-arbre complet maximal trouvé.")
            end_time = time.perf_counter()
            execution_time_ns = (end_time - start_time) * 1e9  # Temps en nanosecondes
            # Fonction pour afficher le temps de manière significative
            if execution_time_ns >= 1e6:  # ≥ 1 ms
                execution_time_ms = execution_time_ns / 1e6
                print(f"Temps d'exécution: {execution_time_ms:.4f} ms.")
            elif execution_time_ns >= 1e3:  # ≥ 1 µs
                execution_time_us = execution_time_ns / 1e3
                print(f"Temps d'exécution: {execution_time_us:.2f} µs.")
            else:  # < 1 µs
                print(f"Temps d'exécution: {execution_time_ns:.0f} ns.")
            # Affichage automatique après recherche
            print("Arbre après recherche du sous-arbre complet maximal :")
            tree.display_breadth_first()
        elif choice == 13:
            value = input("Entrez la valeur du nœud à extraire: ")
            subtree = tree.extract_subtree(value)
            if subtree:
                print(f"Sous-arbre extrait: {subtree.root.value}")
                tree = subtree  # Mettre à jour l'arbre principal avec le sous-arbre extrait
            else:
                print("Sous-arbre non trouvé.")
        elif choice == 14:
            bin_tree = tree.to_binary_tree()
            if bin_tree:
                print("Arbre binaire transformé :")
                bin_tree.display_breadth_first()
            else:
                print("Arbre vide, transformation impossible.")
            # Affichage automatique après transformation
            print("Arbre n-aire original après transformation :")
            tree.display_breadth_first()
        elif choice == 15:
            print("Fin du programme.")
            break
        else:
            print("Choix invalide. Veuillez réessayer.")

if __name__ == "__main__":
    main()