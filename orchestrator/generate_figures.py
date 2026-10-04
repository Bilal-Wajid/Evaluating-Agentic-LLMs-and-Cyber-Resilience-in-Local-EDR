import matplotlib.pyplot as plt
import numpy as np

# IEEE Publication Formatting Standards
plt.style.use('seaborn-v0_8-paper')
plt.rcParams.update({
    'font.size': 8,              
    'font.family': 'serif',
    'axes.labelsize': 8,         
    'xtick.labelsize': 8,        
    'ytick.labelsize': 8,        
    'legend.fontsize': 8,        
    'figure.dpi': 300
})

    
def fig1_capability_vs_latency():
    """Dual-axis bar/line chart with external legend and no title (3B and 8B only)."""
    fig, ax1 = plt.subplots(figsize=(5.0, 2.5))
    
    # Removed TinyLlama, kept 3B and 8B
    models = ['Llama-3.2\n(3B)', 'Llama-3.1\n(8B)']
    mttd = [133.17, 249.68] 
    total_errors = [54, 15] 

    color_bar = '#cccccc'
    color_line = '#000000'

    bars = ax1.bar(models, mttd, color=color_bar, edgecolor='black', width=0.4, label='MTTD (s)')
    ax1.set_ylabel('Mean Time to Detect (s)', color='black')
    ax1.set_ylim(0, 320)

    ax2 = ax1.twinx()
    line = ax2.plot(models, total_errors, color=color_line, marker='o', linestyle='-', linewidth=1.5, label='Total Errors')
    ax2.set_ylabel('Reasoning Errors', color='black')
    ax2.set_ylim(-5, 65)

    lines, labels = ax1.get_legend_handles_labels()
    lines2, labels2 = ax2.get_legend_handles_labels()
    ax1.legend(lines + lines2, labels + labels2, loc='center left', bbox_to_anchor=(1.2, 0.5))

    plt.tight_layout()
    plt.savefig('Fig. 1. Inference Latency vs. Reasoning Fidelity.png', bbox_inches='tight')
    plt.close()

def fig2_camouflage_efficacy():
    """Grouped line chart with no title."""
    fig, ax = plt.subplots(figsize=(3.5, 2.5))
    
    generations = ['Gen 1', 'Gen 2', 'Gen 3']
    cpu_mttd = [120.64, 126.10, 159.83]
    mem_mttd = [106.36, 132.39, 114.36]
    io_mttd = [130.44, 127.92, 180.51]

    ax.plot(generations, cpu_mttd, marker='s', linestyle='-', color='black', linewidth=1.5, label='CPU Virus')
    ax.plot(generations, mem_mttd, marker='^', linestyle='--', color='#555555', linewidth=1.5, label='MEM Virus')
    ax.plot(generations, io_mttd, marker='o', linestyle=':', color='#888888', linewidth=1.5, label='I/O Virus')

    ax.set_ylabel('Mean Time to Detect (s)')
    ax.set_ylim(80, 200)
    ax.legend(loc='upper left')
    
    plt.tight_layout()
    plt.savefig('Fig. 2. Camouflage Efficacy on AI Detection.png', bbox_inches='tight')
    plt.close()

def fig3_cognitive_degradation():
    """Stacked bar chart including all three models with no title and top-left legend."""
    fig, ax = plt.subplots(figsize=(3.5, 2.5))
    
    models = ['TinyLlama\n(1.1B)', 'Llama-3.2\n(3B)', 'Llama-3.1\n(8B)']
    
    policy_fails = np.array([0, 20, 5])
    hallucinations = np.array([0, 34, 10])
    
    bar_width = 0.4
    
    ax.bar(models, policy_fails, color='#ffffff', edgecolor='black', hatch='////', width=bar_width, label='Policy Fails')
    ax.bar(models, hallucinations, bottom=policy_fails, color='#666666', edgecolor='black', width=bar_width, label='Hallucinations')

    ax.set_ylabel('Total Count Across 27 Trials')
    # Legend shifted to upper left to sit perfectly above TinyLlama's empty space
    ax.legend(loc='upper left')
    
    plt.tight_layout()
    plt.savefig('Fig. 3. Breakdown of Agent Reasoning Failures.png', bbox_inches='tight')
    plt.close()

def fig4_out_of_band_resilience():
    """Horizontal bullet chart with no title."""
    fig, ax = plt.subplots(figsize=(3.5, 1.5))
    
    categories = ['Evasion Rate\n(AI Failed)', 'Benign OS Utility\n(Sandbox Succeeded)']
    percentages = [100.0, 100.0]
    
    ax.barh(categories, percentages, color=['#333333', '#dddddd'], edgecolor='black', height=0.5)
    
    ax.set_xlabel('Percentage (%)')
    ax.set_xlim(0, 110)
    
    plt.tight_layout()
    plt.savefig('Fig. 4. Sandbox Efficacy During Agent Failure.png', bbox_inches='tight')
    plt.close()

if __name__ == '__main__':
    fig1_capability_vs_latency()
    fig2_camouflage_efficacy()
    fig3_cognitive_degradation()
    fig4_out_of_band_resilience()
    print("Updated IEEE Figures successfully generated in current directory.")