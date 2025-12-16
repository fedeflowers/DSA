"""
```markdown
# Explanation of the LeetCode Solution for "Maximum Profit from Trading Stocks with Discounts"

## 1. Brief Explanation of the Approach
The solution uses a depth-first search (DFS) strategy to explore a tree structure representing a hierarchy of employees. Each employee has an associated cost (present price) and a future profit. The goal is to maximize the profit from trading stock based on the option to buy or skip purchasing stock from employees, with discounts applied based on parents' decisions.

The algorithm defines a recursive DFS function that computes two scenarios for each employee:
- **If the employee is bought**: The associated cost is halved, and children are considered at discounted prices.
- **If the employee is skipped**: The full price is paid, and children are considered at full prices.

A merging function consolidates the results from the children while checking against the provided budget. The solution iteratively builds up the possible costs and profits from the structure of the tree using the two base cases.

The results are returned in the form of two dictionaries:
- One representing profits assuming the current employee is bought.
- Another representing profits assuming the current employee is skipped.

Finally, the algorithm starts the DFS from the root of the tree (CEO) and calculates the maximum profit possible when the root is skipped, effectively ensuring no discounts apply to the root employee.

## 2. Time and Space Complexity Analysis
- **Time Complexity**: O(N * B), where N is the number of employees (or nodes in the tree) and B is the budget. This complexity arises because for each employee, we traverse through all its children and may have to iterate over every possible cost up to the budget while merging results from sibling employees. Merging costs creates a complexity pattern that scales with both N (nodes) and B (budget).

- **Space Complexity**: O(B), since we maintain a dictionary to keep track of the best profit for each possible cost, which could potentially stretch to the budget limit. Additionally, the call stack from recursive DFS can grow proportionally to the height of the tree (which could be O(N) in the worst case for a skewed tree), but the dominating factor here remains the budget.

## 3. Why This Approach is Efficient
This approach is efficient due to its structured exploration of decisions via recursion combined with dynamic programming principles. It avoids redundant calculations by caching results for already computed scenarios (using dictionaries to keep track of costs and associated profits). By merging results from sibling employees at each level, the algorithm combines solutions effectively without exploring every conceivable combination individually.

The use of a tree representation is advantageous, as it directly captures the hierarchical nature of the problem and allows for a systematic, depth-first exploration that fully takes into account the discounts available based on parent decisions. This leads to an optimal solution leveraging decision-making at each node while respecting the budget constraints.
```

Runtime: undefined
Memory: 18308000
"""


# i would keep one list of prices for each possible decision, the node can either buy or not, if it buys the prices of 
# it's children get discounted, an i keep that list, if it doesnt buy then it stays the same,
# i keep for all nodes doing either decision and then keep the best value with the given budget

from collections import defaultdict
import math

#GEMINI CODE:

class Solution:
    def maxProfit(self, n: int, present: List[int], future: List[int], hierarchy: List[List[int]], budget: int) -> int:
        
        # 1. Build Adjacency List (Tree)
        children = defaultdict(list)
        for u, v in hierarchy:
            children[u - 1].append(v - 1)  # Convert 1-based to 0-based

        # 2. Helper to merge two "Knapsacks"
        # pool_a = {cost: profit}, pool_b = {cost: profit}
        # This combines siblings results while respecting total budget
        def merge_pools(pool_a, pool_b):
            merged = {}
            for c1, p1 in pool_a.items():
                for c2, p2 in pool_b.items():
                    total_c = c1 + c2
                    total_p = p1 + p2
                    if total_c <= budget:
                        # Keep the max profit for this specific total cost
                        merged[total_c] = max(merged.get(total_c, 0), total_p)
            return merged

        # 3. DFS Function
        # Returns TWO dictionaries:
        #   dp_bought: Best {cost: profit} if current node u IS bought (children discounted)
        #   dp_skip:   Best {cost: profit} if current node u IS NOT bought (children full price)
        def dfs(u):
            # Base state for recursion: 0 cost, 0 profit
            # These act as accumulators for the children
            agg_if_u_buys = {0: 0}   
            agg_if_u_skips = {0: 0}

            # --- A. Process all children first (Bottom-Up) ---
            for v in children[u]:
                child_bought, child_skipped = dfs(v)
                
                # If u buys, children get the "child_bought" (discounted) scenario
                agg_if_u_buys = merge_pools(agg_if_u_buys, child_bought)
                
                # If u skips, children MUST use the "child_skipped" (full price) scenario
                agg_if_u_skips = merge_pools(agg_if_u_skips, child_skipped)

            # --- B. Calculate u's decision ---
            
            # SCENARIO 1: Parent of u bought (u gets discount)
            # ------------------------------------------------
            res_if_parent_bought = {}
            
            # Option 1.1: We BUY u (at discount) + Children (discounted)
            cost_u = math.floor(present[u] / 2)
            profit_u = future[u] - cost_u
            
            for c, p in agg_if_u_buys.items():
                if c + cost_u <= budget:
                    res_if_parent_bought[c + cost_u] = p + profit_u
            
            # Option 1.2: We SKIP u + Children (full price)
            for c, p in agg_if_u_skips.items():
                # We take max because we want the best of buying vs skipping u
                res_if_parent_bought[c] = max(res_if_parent_bought.get(c, 0), p)


            # SCENARIO 2: Parent of u skipped (u pays full)
            # -----------------------------------------------
            res_if_parent_skipped = {}
            
            # Option 2.1: We BUY u (full price) + Children (discounted)
            cost_u_full = present[u]
            profit_u_full = future[u] - cost_u_full
            
            for c, p in agg_if_u_buys.items():
                if c + cost_u_full <= budget:
                    res_if_parent_skipped[c + cost_u_full] = p + profit_u_full
            
            # Option 2.2: We SKIP u + Children (full price)
            for c, p in agg_if_u_skips.items():
                res_if_parent_skipped[c] = max(res_if_parent_skipped.get(c, 0), p)

            return res_if_parent_bought, res_if_parent_skipped

        # 4. Start from Root (Employee 1 -> Index 0)
        # The CEO effectively has a "skipped" parent (no discount possible)
        _, root_skipped = dfs(0)
        
        return max(root_skipped.values()) if root_skipped else 0
