import os
import shutil
from pathlib import Path

class StaticSiteGenerator:
    def __init__(self, source_dir="content", output_dir="site"):
        self.source_dir = source_dir
        self.output_dir = output_dir
    
    def create_directories(self):
        """Create necessary directories"""
        Path(self.output_dir).mkdir(exist_ok=True)
        print(f"Created output directory: {self.output_dir}")
    
    def copy_static_files(self):
        """Copy static files (CSS, JS, images)"""
        static_src = os.path.join(self.source_dir, "static")
        static_dest = os.path.join(self.output_dir, "static")
        
        if os.path.exists(static_src):
            shutil.copytree(static_src, static_dest, dirs_exist_ok=True)
            print(f"Copied static files to {static_dest}")
    
    def generate_html_page(self, title, content):
        """Generate a simple HTML page"""
        html = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title}</title>
    <link rel="stylesheet" href="static/style.css">
</head>
<body>
    <header>
        <h1>{title}</h1>
    </header>
    <main>
        {content}
    </main>
    <footer>
        <p>&copy; 2024 Static Site. All rights reserved.</p>
    </footer>
</body>
</html>"""
        return html
    
    def create_sample_site(self):
        """Create a sample static site"""
        self.create_directories()
        
        # Create index page
        home_content = "<h2>Welcome</h2><p>This is a sample static website.</p>"
        index_html = self.generate_html_page("Home", home_content)
        
        with open(os.path.join(self.output_dir, "index.html"), "w") as f:
            f.write(index_html)
        
        # Create about page
        about_content = "<h2>About</h2><p>Information about this site.</p>"
        about_html = self.generate_html_page("About", about_content)
        
        with open(os.path.join(self.output_dir, "about.html"), "w") as f:
            f.write(about_html)
        
        # Create CSS file
        os.makedirs(os.path.join(self.output_dir, "static"), exist_ok=True)
        css_content = """
body {
    font-family: Arial, sans-serif;
    line-height: 1.6;
    margin: 0;
    padding: 20px;
    background-color: #f4f4f4;
}

header {
    background-color: #333;
    color: #fff;
    padding: 10px 0;
    margin-bottom: 20px;
}

main {
    background-color: #fff;
    padding: 20px;
    border-radius: 5px;
}

footer {
    text-align: center;
    margin-top: 20px;
    color: #666;
}
"""
        with open(os.path.join(self.output_dir, "static", "style.css"), "w") as f:
            f.write(css_content)
        
        print("Sample static site created successfully!")

if __name__ == "__main__":
    generator = StaticSiteGenerator()
    generator.create_sample_site()
