import simpy
import random

# Email class representing each email and its analysis scores.
class Email:
    def __init__(self, email_id):
        self.id = email_id
        self.text_score = random.random()
        self.image_score = random.random()
        self.attachment_score = random.random()
        self.classification = None

# Simulate text analysis with a random processing delay.
def text_analysis(env, email):
    processing_time = random.uniform(0.5, 1.5)
    yield env.timeout(processing_time)
    print(f"Time {env.now:.2f}: Email {email.id} text analysis complete.")

# Simulate image analysis with a random processing delay.
def image_analysis(env, email):
    processing_time = random.uniform(0.5, 1.5)
    yield env.timeout(processing_time)
    print(f"Time {env.now:.2f}: Email {email.id} image analysis complete.")

# Simulate attachment analysis with a random processing delay.
def attachment_analysis(env, email):
    processing_time = random.uniform(0.5, 1.5)
    yield env.timeout(processing_time)
    print(f"Time {env.now:.2f}: Email {email.id} attachment analysis complete.")

# Decision engine using the average score of the three analyses.
def decision_engine(email):
    avg_score = (email.text_score + email.image_score + email.attachment_score) / 3
    if avg_score >= 0.8:
        return "Very Probable"
    elif avg_score >= 0.6:
        return "Probable"
    elif avg_score >= 0.3:
        return "Needs Human Intervention"
    else:
        return "Not Probable"

# Process each email through the analysis stages and then classify.
def process_email(env, email):
    print(f"Time {env.now:.2f}: Start processing Email {email.id}")
    yield env.process(text_analysis(env, email))
    yield env.process(image_analysis(env, email))
    yield env.process(attachment_analysis(env, email))
    email.classification = decision_engine(email)
    print(f"Time {env.now:.2f}: Email {email.id} classified as '{email.classification}'\n")

# Generate exactly 3 emails in total.
def email_generator(env, arrival_rate):
    for i in range(3):
        email = Email(i)
        print(f"Time {env.now:.2f}: Generated Email {email.id} with scores -> "
              f"Text: {email.text_score:.2f}, Image: {email.image_score:.2f}, Attachment: {email.attachment_score:.2f}")
        env.process(process_email(env, email))
        # Wait for the next email arrival; interarrival times follow an exponential distribution.
        yield env.timeout(random.expovariate(arrival_rate))

# Set up and run the simulation.
def run_simulation(sim_time, arrival_rate):
    env = simpy.Environment()
    env.process(email_generator(env, arrival_rate))
    env.run(until=sim_time)

if __name__ == "__main__":
    # Run the simulation for 20 time units with an average arrival rate of 1 email per time unit.
    run_simulation(sim_time=20, arrival_rate=1)
