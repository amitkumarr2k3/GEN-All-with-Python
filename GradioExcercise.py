import gradio as gr
def greet(name, intensity):
  return "Hello, " + name + "!" * int(intensity)
demo = gr.Interface(
  fn=greet,
  inputs=["text", "slider"],
  outputs=["text"],
  title = "Greeting Bot",
  description="Say hello to the world!"
)
demo.launch(share=True)