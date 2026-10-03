"""Policy Iteration
Repeatedly:
    1. evaluate current policy
    2. improve current policy
    3. stop when policy becomes stable
"""

from play_4x4_world_game.environment import GridWorld4x4
from play_4x4_world_game.policy import EquiprobableRandomPolicy, GreedyPolicy, Policy
from play_4x4_world_game.policy_evaluation import iterative_policy_evaluation
from play_4x4_world_game.policy_improvement import improve_greedy_policy


def policy_iteration(
    env: GridWorld4x4,
    gamma: float = 1.0,
    theta: float = 1e-6,
) -> tuple[GreedyPolicy, dict[int, float], int]:

    policy: Policy = EquiprobableRandomPolicy(env=env)
    iteration = 0

    while True:
        iteration += 1

        """ 1. Policy Evaluation """
        vpi_values = iterative_policy_evaluation(env, policy, gamma, theta)

        """ 2. Policy Improvement 
        (first π0 - equiprobable then it turned into greedy policy from π1 -> greedy) """
        improved_policy = improve_greedy_policy(env, vpi_values, gamma)

        """ 3. check whether policy changed """
        if _check_policies_equal(env, policy, improved_policy):
            return improved_policy, vpi_values, iteration

        policy = improved_policy


def _check_policies_equal(
    env: GridWorld4x4, policy_a: Policy, policy_b: Policy
) -> bool:

    for state in env.states:
        if env.is_terminal(state):
            continue

        for action in env.actions:
            if policy_a.probability(state, action) != policy_b.probability(
                state, action
            ):
                return False
    return True


# Check and test policy_iteration function
if __name__ == "__main__":
    iterated_improved_policy, vpi_values, iterations = policy_iteration(
        env=GridWorld4x4()
    )
    print(f"{iterated_improved_policy=},\n{vpi_values=}\n{iterations=}")
