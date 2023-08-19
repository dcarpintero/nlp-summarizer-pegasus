import gradio as gr

title = "Text Summarization with google/pegasus-xsum"
examples = [
            ["Diffusion models, introduced in 2015, have emerged as the leading deep generative     models for image, audio, and video synthesis due to their training stability and high-quality sample generation. While other generative models like Generative Adversarial Networks (GANs), Variational Autoencoders (VAEs), and Flow-based models can also produce high-quality images, diffusion models have demonstrated superior performance in their abilities towards training convergence (stability), fine control over noise levels, invertible process and flexibility across domains. In practice, diffusion models operate by gradually adding Gaussian noise to the training data until the data transforms into pure noise. The model then learns to reverse this process by computing the loss between the predicted and effective noise. By applying this learned denoising process to random seeds sampled from a normal distribution, diffusion models can generate data with realistic characteristics. This process is inspired by the concept of diffusion in physics, wherein particles spread and disperse from an area of high concentration to areas of lower concentration through random motion. Similarly, in diffusion models, the gradual introduction of noise can be regarded as a diffusion-like process, where the noise spreads and interacts with the data, gradually transforming it. The iterative steps in the diffusion model mimic the progression of time in a diffusion process, with each step representing a moment of diffusion and information exchange."],
            ["The Transformer is an encoder-decoder architecture aimed at reducing sequential computation (to speed-up the training time). It was introduced by Google and the University of Toronto in 2017, and has been widely used in Natural Language Processing tasks such as machine translation, reading comprehension, abstractive summarization, and text classification. The core contribution of the Transformer is the use a self-attention mechanism, which allows the model to learn the relevance and context of all words (tokens) in an input, not just the neighboring words. It achieves this through attention weights (learned during the training phase) that determine the importance of each word to one another (irrespectively of their position)."]]


pegasus = gr.Interface.load("huggingface/google/pegasus-xsum", 
                            inputs=gr.Textbox(lines=20, placeholder="Content Here..."),
                            outputs=gr.Textbox(lines=20, placeholder="..."),
                            title=title,
                            examples=examples).queue(concurrency_count=2)

pegasus.launch(share=True)

