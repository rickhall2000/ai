# Prompt Engineering Notes
I have seen various videos that talk about prompt engineering, but I have never tried to record the findings. I watch them and then forget. I am going to try to be more deliberate, to try to get a coherent idea of what works best.

## Notes from Prompt Engineering for Improved Performance on Pluralsight

### Elements of a Prompt
* Context - Helps the model understand the task, or the desired output
* Input Data - The data you want the model to process
* Instructions - Textually describe what you want the model to do 
* Examples - Which demonstrate the correct behavior to the model 
* Constraints - Which restrict the output based on specific requirements

### Common Propting Techniques
* Zero-shot learning - the simplest prompt engineering technique. You describe the task you want it to solve and let it generate a response.
* Few-shot learning - Adds input and output examples to the prompt, showing the model the correct behavior.
* Instruction Prompting - Provide specific instructions to the model to produce specific outputs. 

### Causes of Prompting Failures
* Promts that are too vague - Can lead to unpredictable results
* Bias and leading language - Can skew the results 
* Evolving language and knowledge - Chat-GPT has a cutoff date on its training

### More Advanced Techniques
* Chain-of-Thought Prompting - provide a train of thought, or series of reasoning steps to improve the model's ability to perform complext reasoning. Can be combined with few-shot prompting. 
* Knowledge Augmentation - Augment prompts with relevant keywords, structured data, additional context and external data 
* Prompt Tuning - refine and optmize an existing prompt to improve model's output. Can be manual or automatic. Define an objective, and evaluate the response to a prompt, then make changes and evaluate the new results. Most auto-tuning tecniques require changing prompt embeddings, which requires a self-hosted LLM.

### Summarizing text 
- Set context: You are an AI assistant that is expert at summerizing content, your goal is to summarize content based on the given criteria.
- Your content to summarize is: You can pass text or a URL
- Here is the criteria: Could be to summarize for this type of persona, or how many sentences, or what to focus on (eg. cost)

### Expanding text
This looks like responding to me. Take this input, and respond in this way. Say thanks if it was postive, sorry if it was negative. Maybe I don't understand this point enough.

### Text to image generation
- include subject of rendered image, description, style
- include 10+ words
- include subject and multple adjictives
- include style keywords

### Inferring 
Can infer topics, emotion and sentiment. Inferring is gathering information that isn't explicitly stated.

### Text Transformation
- Language Translation
- Spelling and Grammar
- Tone Adjustment
- Text Conversion 

### Factors that impact latency
- The model chosen affects latency - newer tend to be more accurate but slower
- The number of completion tokens requested affects latency
- reduce generated tokens with stop sequences, eg: give me 3 examples 
- max_token attribute
- n attribute how many completions to return (usually 1)
- stream attribute - if true return tokens as soon as available, don't wait for completion