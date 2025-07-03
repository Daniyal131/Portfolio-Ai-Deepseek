from transformers import AutoTokenizer, AutoModelForCausalLM
import torch

print("Starting script...")
print("Loading tokenizer...")
tokenizer = AutoTokenizer.from_pretrained("./deepseek_model")
tokenizer.pad_token = tokenizer.eos_token
print("Tokenizer loaded.")
print("Loading model...")
model = AutoModelForCausalLM.from_pretrained(
    "./deepseek_model",
    device_map="cpu",
    low_cpu_mem_usage=True,
    torch_dtype=torch.float32
)
model.config.pad_token_id = model.config.eos_token_id
print("Model loaded.")

device = torch.device("cpu")
print(f"Using device: {device}")

user_data = {
    "name": "Muhammad Daniyal Khan",
    "education": "B.S. Computer Science, Iqra University",
    "interests": "AI, Full-Stack Development",
    "github": "https://github.com/Daniyal131",
    "linkedin": "https://www.linkedin.com/in/muhammad-daniyal-89a974239/"
}

# prompt = f"""
# Generate a professional, responsive React + Tailwind CSS portfolio page codebase, optimized for mobile and desktop. Use the following user data: {user_data}. Output a single App.jsx file, including Tailwind CSS via CDN (https://cdn.jsdelivr.net/npm/tailwindcss@2.2.19/dist/tailwind.min.css). Create a unique design each time by randomly varying the layout (e.g., flex or grid, single-column or two-column), color scheme (e.g., dark, pastel, or vibrant), and styling (e.g., font sizes, rounded borders, or shadows). Ensure the code is clean, functional, and clearly integrates the user data (e.g., name as a header, education and interests in a section, GitHub and LinkedIn as clickable links). Return only the raw code, with no explanations or comments.
# """

# prompt = f"""
# Create a simple React portfolio page using Tailwind CSS. Include the following user data: {user_data}. The page should show the user's name as a main heading, their education and interests in a section, and clickable links to their GitHub and LinkedIn. Use a clean and minimal layout. Include Tailwind CSS via CDN. Output only the code for a single App.jsx file, with no explanations or comments.
# """



# prompt = f"""
# Generate a minimal and responsive portfolio in React with Tailwind CSS using the following user data: {user_data}.
#
# Only output the code for a single App.jsx file.
# - Keep the layout simple and centered.
# - Include a gradient background or light modern background.
# - Display name as a bold heading, education and interests below it.
# - Add clickable GitHub and LinkedIn links at the bottom.
# - Use variables (no hardcoded values), and ensure a clean visual style using Tailwind classes (rounded corners, spacing, colors).
# - Do not include any extra explanations or comments — just return the clean code.
# """


# prompt = f"""
# Using the following React + Tailwind CSS code as a base, generate a new version of this portfolio component.
# Only change the font family and text sizes slightly to make it look different, but keep the structure, layout, styling, and class names exactly the same.
#
# DON'T GIVE ME THE PREVIOUS CODE JUST GIVE ME THE OUTPUT AND DONOT GIVE ME ANY EXTRA OUTPUT
# I don't want the base code into the output I just want the new generated code in to output only don't include any other thing in the output
#
# Do not change the colors, background, alignment, or spacing. Only update:
# - The font family classes (e.g., font-sans, font-serif)
# - Tailwind text sizes (e.g., text-lg to text-xl)
#
# Use the exact same structure and data. Output only a valid updated App.jsx code block.
#
# Base code:
# import React from "react";
#
# const App = () => {{
#   const user = {{
#     name: "Muhammad Daniyal Khan",
#     education: "B.S. Computer Science, Iqra University",
#     interests: "AI, Full-Stack Development",
#     github: "https://github.com/Daniyal131",
#     linkedin: "https://www.linkedin.com/in/muhammad-daniyal-89a974239/",
#   }};
#
#   return (
#     <div className="min-h-screen flex items-center justify-center bg-gradient-to-br from-indigo-100 via-purple-100 to-pink-100 px-4 py-12">
#       <div className="max-w-xl w-full bg-white rounded-3xl shadow-2xl p-10 transition-transform duration-300 hover:scale-[1.01]">
#         <h1 className="text-4xl font-extrabold text-center text-indigo-700 mb-5 tracking-wide">
#           {{user.name}}
#         </h1>
#         <p className="text-center text-gray-600 text-lg mb-4">{{user.education}}</p>
#         <p className="text-center text-gray-700 text-base mb-8 italic">
#           Interests: {{user.interests}}
#         </p>
#         <div className="flex justify-center space-x-8">
#           <a
#             href={{user.github}}
#             target="_blank"
#             rel="noopener noreferrer"
#             className="text-indigo-600 hover:text-indigo-800 font-semibold border-b-2 border-transparent hover:border-indigo-600 transition duration-300"
#           >
#             GitHub
#           </a>
#           <a
#             href={{user.linkedin}}
#             target="_blank"
#             rel="noopener noreferrer"
#             className="text-indigo-600 hover:text-indigo-800 font-semibold border-b-2 border-transparent hover:border-indigo-600 transition duration-300"
#           >
#             LinkedIn
#           </a>
#         </div>
#       </div>
#     </div>
#   );
# }};
#
# export default App;
# """



prompt = """
Update the following React + Tailwind CSS component to change only:
- font families (use font-serif, font-sans, font-mono)
- text sizes (increase each by one step)

Keep everything else exactly the same: layout, colors, classes, structure, and data.

Return only the updated App.jsx code.

Code:
import React from "react";

const App = () => {
  const user = {
    name: "Muhammad Daniyal Khan",
    education: "B.S. Computer Science, Iqra University",
    interests: "AI, Full-Stack Development",
    github: "https://github.com/Daniyal131",
    linkedin: "https://www.linkedin.com/in/muhammad-daniyal-89a974239/",
  };

  return (
    <div className="min-h-screen flex items-center justify-center bg-gradient-to-br from-indigo-100 via-purple-100 to-pink-100 px-4 py-12">
      <div className="max-w-xl w-full bg-white rounded-3xl shadow-2xl p-10 transition-transform duration-300 hover:scale-[1.01]">
        <h1 className="text-4xl font-extrabold text-center text-indigo-700 mb-5 tracking-wide">
          {user.name}
        </h1>
        <p className="text-center text-gray-600 text-lg mb-4">{user.education}}</p>
        <p className="text-center text-gray-700 text-base mb-8 italic">
          Interests: {user.interests}
        </p>
        <div className="flex justify-center space-x-8">
          <a
            href={user.github}
            target="_blank"
            rel="noopener noreferrer"
            className="text-indigo-600 hover:text-indigo-800 font-semibold border-b-2 border-transparent hover:border-indigo-600 transition duration-300"
          >
            GitHub
          </a>
          <a
            href={user.linkedin}
            target="_blank"
            rel="noopener noreferrer"
            className="text-indigo-600 hover:text-indigo-800 font-semibold border-b-2 border-transparent hover:border-indigo-600 transition duration-300"
          >
            LinkedIn
          </a>
        </div>
      </div>
    </div>
  );
};

export default App;
"""



# prompt = """
#
# Update the following React + Tailwind CSS component with only the following changes:
#
# - Change font families using Tailwind classes like: font-sans, font-serif, or font-mono
# - Increase each text size class by one Tailwind step (e.g., text-lg → text-xl, text-base → text-lg, text-4xl → text-5xl, etc.)
#
# Keep everything else exactly the same:
# - Layout
# - Color classes
# - Class names and Tailwind usage
# - HTML structure
# - React JSX format and data
#
# Avoid these mistakes:
# - Do not remove or rename any user fields (name, education, interests, github, linkedin)
# - Do not change layout or container structure
# - Do not switch to TypeScript or change import/export style
# - Do not remove hover or transition classes
# - Do not change the gradient background
#
# Only return the updated App.jsx code.
#
# Code:
# import React from "react";
#
# const App = () => {
#   const user = {
#     name: "Muhammad Daniyal Khan",
#     education: "B.S. Computer Science, Iqra University",
#     interests: "AI, Full-Stack Development",
#     github: "https://github.com/Daniyal131",
#     linkedin: "https://www.linkedin.com/in/muhammad-daniyal-89a974239/",
#   };
#
#   return (
#     <div className="min-h-screen flex items-center justify-center bg-gradient-to-br from-indigo-100 via-purple-100 to-pink-100 px-4 py-12">
#       <div className="max-w-xl w-full bg-white rounded-3xl shadow-2xl p-10 transition-transform duration-300 hover:scale-[1.01]">
#         <h1 className="text-4xl font-extrabold text-center text-indigo-700 mb-5 tracking-wide">
#           {user.name}
#         </h1>
#         <p className="text-center text-gray-600 text-lg mb-4">{user.education}</p>
#         <p className="text-center text-gray-700 text-base mb-8 italic">
#           Interests: {user.interests}
#         </p>
#         <div className="flex justify-center space-x-8">
#           <a
#             href={user.github}
#             target="_blank"
#             rel="noopener noreferrer"
#             className="text-indigo-600 hover:text-indigo-800 font-semibold border-b-2 border-transparent hover:border-indigo-600 transition duration-300"
#           >
#             GitHub
#           </a>
#           <a
#             href={user.linkedin}
#             target="_blank"
#             rel="noopener noreferrer"
#             className="text-indigo-600 hover:text-indigo-800 font-semibold border-b-2 border-transparent hover:border-indigo-600 transition duration-300"
#           >
#             LinkedIn
#           </a>
#         </div>
#       </div>
#     </div>
#   );
# };
#
# export default App;
#
# """







print("Prompt prepared.")

print("Tokenizing prompt...")
inputs = tokenizer(prompt, return_tensors="pt").to(device)
print("Prompt tokenized.")
print("Generating code...")
try:
    outputs = model.generate(
        **inputs,
        max_length=2048,  # Short for speed
        temperature=1.0,  # Increase randomness
        top_p=0.9,
        do_sample=True,
        num_beams=1
    )
    print("Code generated.")
except Exception as e:
    print(f"Generation failed: {e}")
    raise

print("Decoding output...")
generated_code = tokenizer.decode(outputs[0], skip_special_tokens=True)


print("Output decoded.")
print(generated_code[:300])


# print("Saving to file...")
# with open("App.jsx", "w") as f:
#     f.write(generated_code)
# print("Generated frontend saved as App.jsx")

print("Saving to file...")
with open("App.jsx", "w", encoding="utf-8") as f:
    f.write(generated_code)
print("Generated frontend saved as App.jsx")
