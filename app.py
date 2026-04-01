import gradio as gr
import joblib
import pandas as pd

# 1. Model load
model = joblib.load('house_model.pkl')

def predict(Area, Bedrooms, Bathrooms, Floors, YearBuilt, Location, Condition, Garage):
    input_dict = {
        'Id': 1,
        'Area': Area,
        'Bedrooms': Bedrooms,
        'Bathrooms': Bathrooms,
        'Floors': Floors,
        'YearBuilt': YearBuilt,
        'Location': Location,
        'Condition': Condition,
        'Garage': Garage
    }
    input_df = pd.DataFrame([input_dict])
    
    try:
        prediction = model.predict(input_df)[0]
        # Professional formatting for the output
        return f"Estimated Market Value: ${max(0, prediction):,.2f}"
    except Exception as e:
        return f"Error: {str(e)}"

# --- CUSTOM UI DESIGN ---
# Using a professional "Soft" theme with emerald colors
theme = gr.themes.Soft(
    primary_hue="emerald",
    secondary_hue="slate",
    neutral_hue="slate",
    font=[gr.themes.GoogleFont("Poppins"), "ui-sans-serif", "sans-serif"]
)

with gr.Blocks(theme=theme) as demo:
    gr.Markdown(
        """
        # Real Estate Intelligence Engine
        ### AI-Powered Property Valuation Tool
        *Provide the details below to generate an instant market estimate based on historical data.*
        """
    )
    
    with gr.Row():
        # Left Column: Physical Specs
        with gr.Column():
            gr.Markdown("### Structure Details")
            area = gr.Number(label="Total Area (sqft)", value=1000)
            with gr.Row():
                beds = gr.Slider(1, 10, step=1, label="Bedrooms", value=3)
                baths = gr.Slider(1, 10, step=1, label="Bathrooms", value=2)
            with gr.Row():
                floors = gr.Number(label="Floors", value=1)
                year = gr.Number(label="Year Built", value=2015)
        
        # Right Column: Quality & Location
        with gr.Column():
            gr.Markdown("### Location & Quality")
            loc = gr.Dropdown(["Urban", "Suburban", "Rural"], label="Location Type", value="Suburban")
            cond = gr.Dropdown(["Excellent", "Good", "Fair", "Poor"], label="Building Condition", value="Good")
            gar = gr.Radio(["Yes", "No"], label="Has Garage?", value="No")
            
            submit_btn = gr.Button("Calculate Valuation", variant="primary")

    gr.Markdown("---")
    
    # Output Section
    with gr.Row():
        output = gr.Textbox(label="Analysis Result", placeholder="Estimated price will appear here...")

    # Logic remains the same
    submit_btn.click(
        fn=predict,
        inputs=[area, beds, baths, floors, year, loc, cond, gar],
        outputs=output
    )
    
    gr.Markdown(
        """
        <p style='text-align: center; color: #666;'>
        Developed by Pratham Tripathi | Foundation of AI Technology (Batch: AT-01) Project
        </p>
        """
    )

if __name__ == "__main__":
    demo.launch()
