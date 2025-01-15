import customtkinter as ctk

class CollapsibleSidebar(ctk.CTkFrame):
    def __init__(self, parent, **kwargs):
        super().__init__(parent, **kwargs)
        
        # Sidebar state
        self.sidebar_visible = False
        
        # Sidebar content
        self.sidebar = ctk.CTkFrame(self, width=200, corner_radius=0)
        self.sidebar.grid(row=0, column=1, sticky="ns")
        
        # Add some widgets to the sidebar
        ctk.CTkButton(self.sidebar, text="Option 1").pack(pady=10, padx=10)
        ctk.CTkButton(self.sidebar, text="Option 2").pack(pady=10, padx=10)
        ctk.CTkButton(self.sidebar, text="Option 3").pack(pady=10, padx=10)
        
        # Main content area
        self.main_content = ctk.CTkFrame(self)
        self.main_content.grid(row=0, column=0, sticky="nsew")
        
        ctk.CTkLabel(self.main_content, text="Main Content").pack(pady=20)
        
        # Toggle button
        self.toggle_button = ctk.CTkButton(
            self.main_content,
            text="<",
            width=30,
            command=self.toggle_sidebar
        )
        self.toggle_button.place(relx=1.0, rely=0.95, anchor="se")
        
        # Grid configuration
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)
    
    def toggle_sidebar(self):
        if self.sidebar_visible:
            # Hide the sidebar
            self.sidebar.grid_remove()
            self.grid_columnconfigure(1, weight=0)
            self.toggle_button.configure(text="<")
        else:
            # Show the sidebar
            self.sidebar.grid(row=0, column=1, sticky="ns")
            self.grid_columnconfigure(1, weight=1)
            self.toggle_button.configure(text=">")
        self.sidebar_visible = not self.sidebar_visible
