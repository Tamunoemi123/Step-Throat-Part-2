# Given probabilities
prob_st = 0.2  # Probability that a person has strep throat

# Probabilities of testing positive
prob_st_pos = 0.2 * 0.85      # P(A ∩ B) = P(A) * P(B|A)
prob_nst_pos = 0.8 * 0.02     # P(¬A ∩ B) = P(¬A) * P(B|¬A)

# Total probability of testing positive
prob_positive = prob_st_pos + prob_nst_pos

# Probability of testing positive given strep throat
prob_pos_given_st = 0.85

# Using Bayes' theorem to calculate P(A|B)
prob_result = (prob_st * prob_pos_given_st) / prob_positive

print("Probability of person testing positive having strep throat is:", round(prob_result, 3))
