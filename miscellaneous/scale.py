import matplotlib.pyplot as plt
import pandas as pd

# Redefining the data for AUC values only with parameter counts
data_auc_only = {
    'LLMs': ['TinyBert', 'BERT', 'DeBERTa-V3-Large', 'Sheared-LLaMA-1.3B'],
    'Amazon Fashion': [0.6860, 0.6899, 0.7391, 0.7523],
    'Musical Instruments': [0.6275, 0.6993, 0.7395, 0.7569],
    'Gift Cards': [0.6584, 0.7003, 0.7073, 0.7246],
    'Parameters': [14350248, 109482240, 434012160, 1279887360]  # Parameter counts for the models
}

# Convert the dictionary to a DataFrame
df_auc_only = pd.DataFrame(data_auc_only)

# Define colors for the models and other chart elements
model_colors = ['red', 'green', 'blue', 'purple']
line_color = 'black'
text_background_color = 'lightgrey'

# Setting up the figure and axes for the subplots
fig, axs = plt.subplots(3, 1, figsize=(6, 8))

# Line plots without logarithmic compression on the x-axis
for i, category in enumerate(['Amazon Fashion', 'Musical Instruments', 'Gift Cards']):

    if category == 'Amazon Fashion':
        # Plotting each model's data point in different color and adjusting text positions
        for j, model in enumerate(df_auc_only['LLMs']):
            axs[i].plot(df_auc_only['Parameters'][j], df_auc_only[category][j],
                        marker='o', linestyle='', color=model_colors[j])

            # Adjusting text position
            if model == 'Sheared-LLaMA-1.3B':
                text_pos = (0, -20)  # Left and slightly below for Sheared-LLaMA-1.3B
                axs[i].annotate(model, (df_auc_only['Parameters'][j], df_auc_only[category][j]),
                                textcoords="offset points", xytext=text_pos, ha='center',
                                bbox=dict(boxstyle="round,pad=0.3", fc=text_background_color, alpha=0.7))
            elif model == 'DeBERTa-V3-Large':
                text_pos = (10, -15)  # Right for the first three models
                axs[i].annotate(model, (df_auc_only['Parameters'][j], df_auc_only[category][j]),
                                textcoords="offset points", xytext=text_pos, ha='left',
                                bbox=dict(boxstyle="round,pad=0.3", fc=text_background_color, alpha=0.7))
            elif model == 'BERT':
                text_pos = (12, 5)  # Right for the first three models
                axs[i].annotate(model, (df_auc_only['Parameters'][j], df_auc_only[category][j]),
                                textcoords="offset points", xytext=text_pos, ha='left',
                                bbox=dict(boxstyle="round,pad=0.3", fc=text_background_color, alpha=0.7))
            elif model == 'TinyBert':
                text_pos = (12, -10)  # Right for the first three models
                axs[i].annotate(model, (df_auc_only['Parameters'][j], df_auc_only[category][j]),
                                textcoords="offset points", xytext=text_pos, ha='left',
                                bbox=dict(boxstyle="round,pad=0.3", fc=text_background_color, alpha=0.7))


        # Plotting the connecting line
        axs[i].plot(df_auc_only['Parameters'], df_auc_only[category], marker='', linestyle='-', color=line_color)
        axs[i].set_title(f'{category} AUC')
        axs[i].set_xlabel('Number of Parameters')
        axs[i].set_ylabel('AUC')

    else:
        # Plotting each model's data point in different color and adjusting text positions
        for j, model in enumerate(df_auc_only['LLMs']):
            axs[i].plot(df_auc_only['Parameters'][j], df_auc_only[category][j],
                        marker='o', linestyle='', color=model_colors[j])

            # Adjusting text position
            if model == 'Sheared-LLaMA-1.3B':
                text_pos = (0, -20)  # Left and slightly below for Sheared-LLaMA-1.3B
                axs[i].annotate(model, (df_auc_only['Parameters'][j], df_auc_only[category][j]),
                                textcoords="offset points", xytext=text_pos, ha='center',
                                bbox=dict(boxstyle="round,pad=0.3", fc=text_background_color, alpha=0.7))
            elif model == 'DeBERTa-V3-Large':
                text_pos = (10, -15)  # Right for the first three models
                axs[i].annotate(model, (df_auc_only['Parameters'][j], df_auc_only[category][j]),
                                textcoords="offset points", xytext=text_pos, ha='left',
                                bbox=dict(boxstyle="round,pad=0.3", fc=text_background_color, alpha=0.7))
            elif model == 'BERT':
                text_pos = (10, -12)  # Right for the first three models
                axs[i].annotate(model, (df_auc_only['Parameters'][j], df_auc_only[category][j]),
                                textcoords="offset points", xytext=text_pos, ha='left',
                                bbox=dict(boxstyle="round,pad=0.3", fc=text_background_color, alpha=0.7))
            elif model == 'TinyBert':
                text_pos = (12, 2)  # Right for the first three models
                axs[i].annotate(model, (df_auc_only['Parameters'][j], df_auc_only[category][j]),
                                textcoords="offset points", xytext=text_pos, ha='left',
                                bbox=dict(boxstyle="round,pad=0.3", fc=text_background_color, alpha=0.7))

        # Plotting the connecting line
        axs[i].plot(df_auc_only['Parameters'], df_auc_only[category], marker='', linestyle='-', color=line_color)
        axs[i].set_title(f'{category} AUC')
        axs[i].set_xlabel('Number of Parameters')
        axs[i].set_ylabel('AUC')


# Adjust layout for all plots
plt.tight_layout()

# Save the plots as a PDF file without logarithmic compression
adjusted_auc_line_charts_pdf_filename = 'scale.pdf'
plt.savefig(adjusted_auc_line_charts_pdf_filename, bbox_inches='tight')

# # Display the plots
# plt.show()
