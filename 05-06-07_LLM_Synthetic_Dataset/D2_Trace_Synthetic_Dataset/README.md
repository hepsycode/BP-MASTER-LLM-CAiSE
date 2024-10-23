# Large Language Model Synthetic Dataset

LLM synthetic dataset generation uses pre-trained LLM to create synthetic datasets that mimic real-world data. This method leverages the extensive knowledge and contextual understanding embedded in LLMs to generate data that can be used for training, validation, and testing of various ML models. Furthermore, LLM synthetic dataset generation effectively addresses the challenges of reducing the time and effort to collect traces, representing realistic designer behavior, and overcoming security concerns, privacy regulations, and industry restrictions. By leveraging the advanced capabilities of LLMs, our proposed approach provides a robust solution for creating high-quality, relevant, and secure datasets, thereby enhancing the development and performance of ML models.

In such a context, our work used four LLMs as instances of the proposed LLM component in the proposed approach: (1) Gemini, developed by Google DeepMind; (2) GPT3.5, available for free and developed by OpenAI; (3) GPT-4 Turbo}, the professional version of GPT also developed by OpenAI; (4) LLaMA3 70B developed by Meta. 

GPT-4, GPT-3.5 and Gemini are proprietary, meaning their underlying details and weights are not shared publicly. They are generally accessed via paid APIs or cloud services. LLama3 is an open-source model, offering transparency and flexibility with its publicly available architecture and weights. We selected these LLMs because they represent the best proprietary and open-source technologies according to LMSYS LeaderBoard.

The folder D2 folder contains the dataset generated with the LLMs listed above. Prompt schemas are added in word files.
