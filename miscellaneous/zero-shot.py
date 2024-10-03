# # import matplotlib.pyplot as plt
# #
# # # Let's update the provided code to reflect the new data for multi-domain models from the image.
# #
# # # New data from the image for multi-domain models
# # multi_domain_models = ['Shared Bottom', 'MMoE', 'PLE', 'STAR', 'Uni-CTR']
# # multi_domain_auc_values = [0.5543, 0.5713, 0.5724, 0.5636, 0.6391]
# #
# # # Creating the bar plot for multi-domain models
# # plt.figure(figsize=(6, 6))
# # multi_domain_bars = plt.bar(multi_domain_models, multi_domain_auc_values, color='lightgreen')
# #
# # # Adding the AUC values on top of the bars
# # for bar in multi_domain_bars:
# #     yval = bar.get_height()
# #     plt.text(bar.get_x() + bar.get_width()/2, yval + 0.0001, round(yval,4), ha='center', va='bottom')
# #
# # # Setting the title and labels
# # plt.title('AUC Values for Multi-Domain Models')
# # plt.xlabel('Models')
# # plt.ylabel('AUC')
# # plt.ylim(0.4000, 0.675) # Set the limit a bit lower/higher than min/max for aesthetics
# #
# # # Save the plot as a PDF file
# # multi_domain_pdf_filename = '../auc_values_multi_domain_models.pdf'
# # plt.savefig(multi_domain_pdf_filename, bbox_inches='tight')
# #
# # # Display the plot
# # plt.show()
# #
# # # Return the path to the saved PDF file
# # multi_domain_pdf_filename
#
# # Re-importing the required library as the execution state has been reset
#
# import matplotlib.pyplot as plt
#
# # Data from the image for single-domain models
# single_domain_models = ['PNN', 'DCN', 'DeepFM', 'xDeepFM', 'AutoInt', 'FiBiNET']
# single_domain_auc_values = [0.5006, 0.5024, 0.5043, 0.5034, 0.5012, 0.5026]
#
# # Data for multi-domain models
# multi_domain_models = ['Shared\nBottom', 'MMoE', 'PLE', 'STAR', 'Uni-CTR']
# multi_domain_auc_values = [0.5543, 0.5713, 0.5724, 0.5636, 0.6391]
#
# # Setting up the figure and axes for the subplots
# fig, axs = plt.subplots(1, 2, figsize=(9, 5))
#
# # Colors
# color_single_domain = 'yellowgreen'
# color_multi_domain = 'cornflowerblue'
# color_uni_ctr = 'indianred'
#
# # Update the bar plot for single-domain models with new colors
# axs[0].bar(single_domain_models, single_domain_auc_values, color=color_single_domain)
# # axs[0].set_title('AUC Values for Single-Domain Models')
# axs[0].set_xlabel('Models')
# axs[0].set_ylabel('AUC')
# axs[0].set_ylim(0.4000, 0.675)
#
# # Adding the AUC values on top of the bars for single-domain models
# for i, v in enumerate(single_domain_auc_values):
#     axs[0].text(i, v + 0.0001, round(v, 4), ha='center', va='bottom')
#
# # Update the bar plot for multi-domain models with new colors, differentiating Uni-CTR
# for i, model in enumerate(multi_domain_models):
#     if model == 'Uni-CTR':
#         axs[1].bar(model, multi_domain_auc_values[i], color=color_uni_ctr)
#         axs[1].text(i, multi_domain_auc_values[i] + 0.0001, round(multi_domain_auc_values[i], 4), ha='center', va='bottom')
#     else:
#         axs[1].bar(model, multi_domain_auc_values[i], color=color_multi_domain)
#         axs[1].text(i, multi_domain_auc_values[i] + 0.0001, round(multi_domain_auc_values[i], 4), ha='center', va='bottom')
#
# axs[1].set_title('AUC Values for Multi-Domain Models')
# axs[1].set_xlabel('Models')
# axs[1].set_ylim(0.4000, 0.675)
#
# # Layout adjustment
# plt.tight_layout()
#
# # Save the plots as a PDF file to a valid path
# combined_pdf_filename = 'miscellaneous/auc_values_combined.pdf'
# plt.savefig(combined_pdf_filename, bbox_inches='tight')
#
# # # Display the plots
# # plt.show()
# #
# # # Return the path to the saved PDF file
# # combined_pdf_filename


import matplotlib.pyplot as plt

# Data for single-domain models
single_domain_models = ['PNN', 'DCN', 'DeepFM', 'xDeepFM', 'AutoInt', 'FiBiNET']
single_domain_auc_values = [0.5006, 0.5024, 0.5043, 0.5034, 0.5012, 0.5026]

# Data for multi-domain models
multi_domain_models = ['Shared\nBottom', 'MMoE', 'PLE', 'STAR', 'Uni-CTR']
multi_domain_auc_values = [0.5543, 0.5713, 0.5724, 0.5636, 0.6391]

# Colors
color_single_domain = 'yellowgreen'
color_multi_domain = 'cornflowerblue'
color_uni_ctr = 'indianred'

# Setting up the figure for the combined plot
plt.figure(figsize=(8, 6))

# Plotting single-domain models
single_domain_bars = plt.bar(
    [x - 0.2 for x in range(len(single_domain_models))],
    single_domain_auc_values,
    width=0.4,
    color=color_single_domain,
    label='Single-Domain'
)

# Plotting multi-domain models
multi_domain_bars = plt.bar(
    [x + len(single_domain_models) - 0.2 for x in range(len(multi_domain_models))],
    multi_domain_auc_values,
    width=0.4,
    color=color_multi_domain,
    label='Multi-Domain'
)

# Highlighting Uni-CTR
plt.bar(
    len(single_domain_models) + len(multi_domain_models) - 1 - 0.2,
    multi_domain_auc_values[-1],
    width=0.4,
    color=color_uni_ctr,
    label='Uni-CTR'
)

# Adding the AUC values on top of the bars
for bar in single_domain_bars + multi_domain_bars:
    yval = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2, yval + 0.0001, round(yval, 4), ha='center', va='bottom')

# Setting the title and labels
# plt.title('AUC Values for Single-Domain and Multi-Domain Models')
# plt.xlabel('Models')
plt.ylabel('AUC')
plt.xticks(
    [r + 0.1 for r in range(len(single_domain_models) + len(multi_domain_models))],
    single_domain_models + multi_domain_models,
    rotation=45,
    ha='right'
)
plt.ylim(0.4000, 0.675)

# Adding legend
plt.legend()

# Save the combined plot as a PDF file
corrected_pdf_filename = 'miscellaneous/zeroshot.pdf'
plt.savefig(corrected_pdf_filename, bbox_inches='tight')

# Closing the plot to ensure it's correctly saved
plt.close()

# File path
print("PDF file saved at:", corrected_pdf_filename)
