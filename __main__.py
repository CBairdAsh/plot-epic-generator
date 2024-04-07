# __main__.py
from .character_generator import CharacterGenerator
from .plot_generator import PlotGenerator

def main():
    print("Generating a plot...")
    
    plot_summary = PlotGenerator.generate_plot()
    print(plot_summary)

if __name__ == "__main__":
    main()