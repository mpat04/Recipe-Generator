import customtkinter
import os
import openai

# System settings
customtkinter.set_appearance_mode("Dark")
customtkinter.set_default_color_theme("green")

class MyCheckboxFrame(customtkinter.CTkFrame):
    def __init__(self, master, title, values):
        super().__init__(master)
        self.grid_columnconfigure(0, weight=1)
        self.values = values
        self.title = title
        self.checkboxes = []

        self.title = customtkinter.CTkLabel(self, text=self.title, fg_color="gray30", corner_radius=6)
        self.title.grid(row=0, column=0, padx=10, pady=(10, 0), sticky="ew")

        for i, value in enumerate(self.values):
            checkbox = customtkinter.CTkCheckBox(self, text=value)
            checkbox.grid(row=i+1, column=0, padx=10, pady=(10, 0), sticky="w")
            self.checkboxes.append(checkbox)
    
    # function to retrieve user inputs in GUI
    def get(self):
        checked_checkboxes = []
        for checkbox in self.checkboxes:
            if checkbox.get() == 1:
                checked_checkboxes.append(checkbox.cget("text"))
        return checked_checkboxes

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.title("Recipe Bot")
        self.geometry("1000x600")
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure((0, 1), weight=1)
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)
        self.columnconfigure(2, weight=1)
        self.rowconfigure(0, weight=1)
        self.rowconfigure(1, weight=1)
        self.rowconfigure(2, weight=1)

        # Label on app
        label_title = customtkinter.CTkLabel(self, text="Recipe Bot", font=customtkinter.CTkFont(size=50, weight="bold"))
        label_title.grid(row=0, column=0, columnspan=3, pady=10, padx=10, sticky="n")

        # Add cuisine frame
        self.cuisineframe = MyCheckboxFrame(self, "Cuisines",
                                            values=["Asian", "Italian", "Mexican", "Mediterranean", "Indian", "American", "Any"])
        self.cuisineframe.grid(row=1, column=0, pady=(10, 0), padx=10, sticky="nsew")

        # Add dietary restrictions frame
        self.diets = MyCheckboxFrame(self, "Dietary Restrictions",
                                     values=["Vegetarian", "Pollotarian", "Pescatarian", "No Red Meat", "Vegan", "Gluten Free"])
        self.diets.grid(row=1, column=1, pady=(10, 0), padx=(0, 10), sticky="nsew")

        # Add textbox for ingredients
        self.ingredients = customtkinter.CTkEntry(self,
                                                  placeholder_text="Enter Ingredients you want to use!",
                                                  width=100, height=100)
        self.ingredients.grid(row=2, column=0, columnspan=2, pady=10, padx=10, sticky="nsew")

        # Output Frame
        self.outputframe = customtkinter.CTkFrame(self)
        self.outputframe.rowconfigure(0, weight=1)
        self.outputframe.columnconfigure(0, weight=1)
        self.outputframe.columnconfigure(1, weight=1)
        self.outputframe.rowconfigure(1, weight=3)
        self.outputframe.grid(row=1, column=2, rowspan=2, sticky="nsew")

        # buttons
        self.gen_button = customtkinter.CTkButton(self.outputframe, text="Generate Recipe", command=self.generate_recipe)
        self.clear_button = customtkinter.CTkButton(self.outputframe, text="Clear", command=self.clear_all)
        self.gen_button.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")
        self.clear_button.grid(row=0, column=1, padx=10, pady=10, sticky="nsew")

        # textbox
        self.recipebox = customtkinter.CTkTextbox(self.outputframe, wrap=customtkinter.WORD)
        self.recipebox.grid(row=1, columnspan=2, padx=10, pady=10, sticky="nsew")

    # button functions to clear input areas and generate recipes using user input
    def clear_all(self):
        for checkbox in self.cuisineframe.checkboxes:
            checkbox.deselect()
        for checkbox in self.diets.checkboxes:
            checkbox.deselect()
        self.ingredients.delete(0, "end")
        self.recipebox.delete("1.0", "end")

    def generate_recipe(self):
        ingredients = self.ingredients.get()
        cuisine = self.cuisineframe.get()
        diet = self.diets.get()

        # clear recipe box to generate new recipe
        self.recipebox.delete("1.0", "end")

        prompt = "Please generate a recipe with the following requirements. "
        prompt += f" Ingredients I have: {ingredients}. "
        prompt += f" The cuisine I want: {cuisine}. "
        prompt += f" My dietary restriction: {diet}."

        # Updated API client usage
        openai.api_key = os.getenv("OPENAI_API_KEY")
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "user", "content": prompt}
            ]
        )
        answer = response['choices'][0]['message']['content']
        self.recipebox.insert("1.0", answer)

if __name__ == "__main__":
    app = App()
    app.mainloop()
