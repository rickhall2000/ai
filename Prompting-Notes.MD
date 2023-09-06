# Prompt Engineering Notes
I have seen various videos that talk about prompt engineering, but I have never tried to record the findings. I watch them and then forget. I am going to try to be more deliberate, to try to get a coherent idea of what works best.

## Notes from Prompt Engineering for Improved Performance on Pluralsight

Elements of a Prompt
* Context - Helps the model understand the task, or the desired output
* Input Data - The data you want the model to process
* Instructions - Textually describe what you want the model to do 
* Examples - Which demonstrate the correct behavior to the model 
* Constraints - Which restrict the output based on specific requirements

Common Propting Techniques
* Zero-shot learning - the simplest prompt engineering technique. You describe the task you want it to solve and let it generate a response.
* Few-shot learning - Adds input and output examples to the prompt, showing the model the correct behavior.
* Instruction Prompting - Provide specific instructions to the model to produce specific outputs. 

Causes of Prompting Failures
* Promts that are too vague - Can lead to unpredictable results
* Bias and leading language - Can skew the results 
* Evolving language and knowledge - Chat-GPT has a cutoff date on its training

More Advanced Techniques
* Chain-of-Thought Prompting - provide a train of thought, or series of reasoning steps to improve the model's ability to perform complext reasoning. Can be combined with few-shot prompting. 
* Knowledge Augmentation - Augment prompts with relevant keywords, structured data, additional context and external data 
* Prompt Tuning - refine and optmize an existing prompt to improve model's output. Can be manual or automatic. Define an objective, and evaluate the response to a prompt, then make changes and evaluate the new results. Most auto-tuning tecniques require changing prompt embeddings, which requires a self-hosted LLM.







