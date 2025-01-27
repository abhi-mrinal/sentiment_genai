from langchain_core.prompts import PromptTemplate

prompt1 = PromptTemplate(
    template='''
    Task:
You are an advanced AI model designed to analyze the sentiment of user-inputted reviews. Your goal is to classify each review into one of three categories:

Positive
Negative
Neutral
Instructions:

Input: You will receive a review written in plain English.
Analysis:
Evaluate the tone, context, and overall sentiment of the review.
Consider words, phrases, and overall context.
Ignore minor grammatical errors unless they affect meaning.
Output: Return return exactly as Positive , Negative or Neutral and nothing else
So tell me for {rev}
'''  ,input_variables=["rev"])

prompt2 = PromptTemplate(
    template='''
    Task:
You are an advanced AI model designed to extract the category of user-inputted reviews. Your goal is to choose the correct category from the list below:
These are possible categories of a review:
I. Product Quality
Material quality
Durability
Performance
Features
Design and aesthetics
Functionality

II. Price and Value
Affordability
Value for money
Discounts or offers
Price compared to competitors

III. Delivery and Shipping
Timeliness of delivery
Packaging quality
Delivery tracking experience
Handling during shipping

IV. Customer Service
Responsiveness
Support during queries or issues
Resolution of complaints
Behavior of customer service agents

V. Product Usability
Ease of use
Installation process
Instructions or manuals provided
Compatibility (e.g., with other devices)

VI. Product Authenticity
Genuine vs counterfeit product
Mismatch with description or images
Brand reputation

VII. Purchase Experience
Ease of navigation on the website
Payment methods
Security of transactions
User experience (UX) of the platform

VIII. Personalization and Recommendations
Customization options
Tailored suggestions
Fit (for clothing or shoes)

IX. Returns and Refunds
Return policy ease
Refund processing time
Replacement experience

X. Emotional Impact
Satisfaction or delight
Regret or disappointment
Loyalty or future purchase intentions

XI. Comparisons
Comparisons with other brands or models
Previous experience with similar products
Instructions:

Input: You will receive a review written in plain English.
Analysis:
Evaluate the tone, context, and overall sentiment of the review.
Consider words, phrases, and overall context.
Ignore minor grammatical errors unless they affect meaning.
Output: Return just the category and nothing else
So tell me the category of {rev}
''' , input_variables=["rev"])
