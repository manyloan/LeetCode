from typing import List
import time

###  Solução 1
class Solution:
    def twoSum_solucao1(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        for i in range(n-1):
            for j in range(i+1, n):
                if nums[i] + nums[j] == target:
                    return [i,j]
        return []

    def twoSum_solucao2(self, nums: List[int], target: int) -> List[int]:
        numMap = {}
        n = len(nums)

        for i in range(n):
            complement = target - nums[i]
            if complement in numMap:
                return [numMap[complement], i]
            numMap[nums[i]] = i

        return []  # No solution found
    

lista = [i for i in range(9888)]

# Adicionando os dois últimos itens que somados dão 933
lista.append(13333)
lista.append(80000)

solution_instance = Solution()

start_time1 = time.time()
print(solution_instance.twoSum_solucao1(lista, target=93333))
end_time1 = time.time()
execution_time1 = end_time1 - start_time1
print("Tempo de execução:", execution_time1, "segundos")

start_time2 = time.time()
print(solution_instance.twoSum_solucao2(lista, target=93333))
end_time2 = time.time()
execution_time2 = end_time2 - start_time2
print("Tempo de execução:", execution_time2, "segundos")

if execution_time2 < execution_time1:
    print(f"Solucao 2 foi {round((execution_time1/execution_time2),1)} vezes mais rápido")
else:
    print(f"Solucao 1 foi {round((execution_time2/execution_time1),1)} vezes mais rápido")
