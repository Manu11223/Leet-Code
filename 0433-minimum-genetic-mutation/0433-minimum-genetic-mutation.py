from collections import deque

class Solution:
    def minMutation(self, startGene: str, endGene: str, bank: list[str]) -> int:
        bank_set = set(bank)
        if endGene not in bank_set:
            return -1

        genes = "ACGT"
        visited = {startGene}
        queue = deque([(startGene, 0)])

        while queue:
            gene, steps = queue.popleft()
            if gene == endGene:
                return steps

            gene_chars = list(gene)
            for i in range(8):
                original = gene_chars[i]
                for c in genes:
                    if c == original:
                        continue
                    gene_chars[i] = c
                    candidate = ''.join(gene_chars)
                    if candidate in bank_set and candidate not in visited:
                        visited.add(candidate)
                        queue.append((candidate, steps + 1))
                gene_chars[i] = original  # restore before next position

        return -1