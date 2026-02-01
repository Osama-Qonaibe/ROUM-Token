#!/usr/bin/env python3
"""
ROUM Token - CertiK Audit Charts Generator
Generates professional security audit visualization charts

Author: Osama Qonaibe
License: MIT
Repository: https://github.com/Osama-Qonaibe/ROUM-Token
"""

import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import Wedge, FancyBboxPatch
import numpy as np
import os

plt.style.use('default')
plt.rcParams['font.family'] = 'DejaVu Sans'
plt.rcParams['figure.facecolor'] = 'white'
plt.rcParams['axes.facecolor'] = 'white'

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
CHARTS_DIR = os.path.join(BASE_DIR, '..', 'assets', 'charts')

BRAND_COLOR = '#00cc44'
DPI = 300

def ensure_charts_directory():
    if not os.path.exists(CHARTS_DIR):
        os.makedirs(CHARTS_DIR)
        print(f"✅ Created directory: {CHARTS_DIR}")

def save_chart(filename, message):
    plt.tight_layout()
    filepath = os.path.join(CHARTS_DIR, filename)
    plt.savefig(filepath, dpi=DPI, bbox_inches='tight', facecolor='white', edgecolor='none')
    plt.close()
    print(f"   ✅ {filename}")
    return filename

def create_security_score_gauge():
    print("Creating Chart 1/7: Security Score Dashboard...")
    
    fig, ax = plt.subplots(figsize=(12, 10), facecolor='white')
    ax.set_xlim(-1.5, 1.5)
    ax.set_ylim(-0.5, 1.8)
    ax.axis('off')
    
    ax.text(0, 1.65, 'ROUM Token - CertiK Security Audit', 
            ha='center', fontsize=22, fontweight='bold', color='#1a1a1a')
    ax.text(0, 1.5, 'Overall Security Score', 
            ha='center', fontsize=14, color='#666666')
    
    colors = ['#ff4444', '#ff8800', '#ffcc00', '#88cc00', BRAND_COLOR]
    score = 97
    
    start_angle = 180
    
    for i in range(5):
        theta1 = start_angle - (i * 36)
        theta2 = start_angle - ((i + 1) * 36)
        wedge = Wedge((0, 0), 1, theta2, theta1, 
                     width=0.25, facecolor=colors[i], 
                     edgecolor='white', linewidth=3)
        ax.add_patch(wedge)
    
    score_angle = start_angle - (score * 1.8)
    angle_rad = np.radians(score_angle)
    needle_length = 0.85
    ax.plot([0, needle_length * np.cos(angle_rad)], 
            [0, needle_length * np.sin(angle_rad)],
            color='#333333', linewidth=5, solid_capstyle='round', zorder=10)
    
    circle = plt.Circle((0, 0), 0.08, color='#333333', zorder=11)
    ax.add_patch(circle)
    
    ax.text(0, -0.15, '97', ha='center', fontsize=80, 
            fontweight='bold', color=BRAND_COLOR)
    ax.text(0.35, -0.15, '/100', ha='left', fontsize=24, color='#666666')
    ax.text(0, -0.35, 'EXCELLENT', ha='center', fontsize=16, 
            fontweight='bold', color=BRAND_COLOR,
            bbox=dict(boxstyle='round,pad=0.4', facecolor='#e8f5e9', 
                     edgecolor=BRAND_COLOR, linewidth=2))
    
    metrics = [
        ('Code Quality', 97),
        ('Security Features', 98),
        ('Gas Optimization', 97),
        ('Standards Compliance', 100)
    ]
    
    y_start = -0.6
    for i, (label, value) in enumerate(metrics):
        y = y_start - (i * 0.22)
        ax.text(-1.3, y, label, ha='left', fontsize=11, color='#333333')
        ax.text(1.3, y, f'{value}/100', ha='right', fontsize=11, 
                fontweight='bold', color=BRAND_COLOR)
        
        bar_start = -0.8
        bar_width = (value / 100) * 1.6
        rect = FancyBboxPatch((bar_start, y - 0.05), bar_width, 0.1,
                             boxstyle="round,pad=0.01", 
                             facecolor=BRAND_COLOR, edgecolor='none', alpha=0.7)
        ax.add_patch(rect)
    
    approval_text = '✅ APPROVED FOR MAINNET DEPLOYMENT'
    ax.text(0, -1.55, approval_text, ha='center', fontsize=12, 
            fontweight='bold', color=BRAND_COLOR,
            bbox=dict(boxstyle='round,pad=0.6', facecolor='#e8f5e9', 
                     edgecolor=BRAND_COLOR, linewidth=2))
    
    return save_chart('certik_score_dashboard.png', 'Security Score Dashboard')

def create_industry_comparison():
    print("Creating Chart 2/7: Industry Comparison...")
    
    fig, ax = plt.subplots(figsize=(12, 8), facecolor='white')
    
    tokens = ['ROUM Token', 'Ethereum (ETH)', 'BNB', 'USDC', 'USDT']
    scores = [97, 95, 92, 90, 88]
    colors = [BRAND_COLOR, '#627EEA', '#F3BA2F', '#2775CA', '#26A17B']
    
    y_pos = np.arange(len(tokens))
    bars = ax.barh(y_pos, scores, color=colors, edgecolor='white', 
                   linewidth=2, height=0.7)
    
    for i, (score, bar) in enumerate(zip(scores, bars)):
        width = bar.get_width()
        if i == 0:
            ax.text(width + 1, bar.get_y() + bar.get_height()/2, 
                    f'{score}/100 ★ #1', ha='left', va='center',
                    fontsize=12, fontweight='bold', color=BRAND_COLOR)
            bar.set_edgecolor(BRAND_COLOR)
            bar.set_linewidth(3)
        else:
            ax.text(width + 1, bar.get_y() + bar.get_height()/2, 
                    f'{score}/100', ha='left', va='center',
                    fontsize=11, color='#333333')
    
    ax.set_yticks(y_pos)
    ax.set_yticklabels(tokens, fontsize=12, fontweight='bold')
    ax.set_xlabel('Security Score', fontsize=12, fontweight='bold', color='#333333')
    ax.set_xlim(0, 105)
    ax.set_ylim(-0.7, len(tokens) - 0.3)
    
    ax.grid(axis='x', alpha=0.3, linestyle='--', linewidth=0.5)
    ax.set_axisbelow(True)
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['left'].set_linewidth(1.5)
    ax.spines['bottom'].set_linewidth(1.5)
    
    ax.text(0.5, 1.05, 'Industry Leadership Position', 
            transform=ax.transAxes, ha='center', fontsize=18, 
            fontweight='bold', color='#1a1a1a')
    ax.text(0.5, 1.0, 'Security Comparison - ROUM leads with 97/100', 
            transform=ax.transAxes, ha='center', fontsize=12, color='#666666')
    
    return save_chart('industry_comparison.png', 'Industry Comparison')

def create_test_results():
    print("Creating Chart 3/7: Test Results...")
    
    fig, ax = plt.subplots(figsize=(10, 10), facecolor='white')
    
    sizes = [95.65, 4.35]
    labels = ['Passed Tests\\n22', 'Attention\\n1']
    colors = [BRAND_COLOR, '#ff8800']
    explode = (0.05, 0)
    
    wedges, texts, autotexts = ax.pie(sizes, labels=labels, colors=colors,
                                        autopct='%1.1f%%', startangle=90,
                                        explode=explode, 
                                        textprops={'fontsize': 14, 'fontweight': 'bold'},
                                        pctdistance=0.85, 
                                        wedgeprops={'width': 0.4, 'edgecolor': 'white', 
                                                   'linewidth': 3})
    
    for autotext in autotexts:
        autotext.set_color('white')
        autotext.set_fontsize(16)
        autotext.set_fontweight('bold')
    
    centre_circle = plt.Circle((0, 0), 0.60, fc='white', linewidth=3, 
                              edgecolor=BRAND_COLOR)
    ax.add_artist(centre_circle)
    
    ax.text(0, 0.15, '95.65%', ha='center', va='center', 
            fontsize=48, fontweight='bold', color=BRAND_COLOR)
    ax.text(0, -0.05, 'Pass Rate', ha='center', va='center', 
            fontsize=16, color='#666666')
    ax.text(0, -0.25, '22/23', ha='center', va='center', 
            fontsize=14, fontweight='bold', color='#333333')
    
    ax.text(0, 1.35, 'CertiK Audit Test Results', 
            ha='center', fontsize=18, fontweight='bold', color='#1a1a1a')
    ax.text(0, 1.20, '22 out of 23 tests passed', 
            ha='center', fontsize=12, color='#666666')
    
    legend_elements = [
        plt.Line2D([0], [0], marker='o', color='w', markerfacecolor=BRAND_COLOR, 
                   markersize=12, label='✅ Passed: 22 tests'),
        plt.Line2D([0], [0], marker='o', color='w', markerfacecolor='#ff8800', 
                   markersize=12, label='⏳ Attention: 1 item (Pre-launch)')
    ]
    ax.legend(handles=legend_elements, loc='upper left', 
             bbox_to_anchor=(-0.15, -0.05), fontsize=11, frameon=True, 
             fancybox=True, shadow=True)
    
    ax.text(0, -1.25, '0 Critical, High, Medium, or Low Risk Issues', 
            ha='center', fontsize=11, fontweight='bold', color=BRAND_COLOR,
            bbox=dict(boxstyle='round,pad=0.5', facecolor='#e8f5e9', 
                     edgecolor=BRAND_COLOR, linewidth=2))
    
    ax.axis('equal')
    return save_chart('test_results.png', 'Test Results')

def create_risk_assessment():
    print("Creating Chart 4/7: Risk Assessment...")
    
    fig, ax = plt.subplots(figsize=(12, 8), facecolor='white')
    
    categories = ['Critical\\nIssues', 'High\\nRisk', 'Medium\\nRisk', 
                  'Low\\nRisk', 'Alerts', 'Safe/\\nSecure']
    values = [0, 0, 0, 0, 0, 22]
    colors = ['#ff4444', '#ff8800', '#ffcc00', '#88cc00', '#4488ff', BRAND_COLOR]
    
    bars = ax.barh(categories, values, color=colors, edgecolor='white', 
                   linewidth=2, height=0.7)
    
    for bar, val in zip(bars, values):
        width = bar.get_width()
        if val > 0:
            ax.text(width + 0.3, bar.get_y() + bar.get_height()/2, 
                    f'{val}', ha='left', va='center',
                    fontsize=14, fontweight='bold', color='#333333')
        else:
            ax.text(0.3, bar.get_y() + bar.get_height()/2, 
                    '0 ✓', ha='left', va='center',
                    fontsize=12, fontweight='bold', color=BRAND_COLOR)
    
    for i in range(len(bars) - 1):
        bars[i].set_alpha(0.3)
    
    bars[-1].set_edgecolor(BRAND_COLOR)
    bars[-1].set_linewidth(3)
    
    ax.set_xlim(0, 25)
    ax.set_xlabel('Number of Issues', fontsize=12, fontweight='bold', 
                  color='#333333')
    ax.grid(axis='x', alpha=0.3, linestyle='--', linewidth=0.5)
    ax.set_axisbelow(True)
    
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['left'].set_linewidth(1.5)
    ax.spines['bottom'].set_linewidth(1.5)
    
    ax.text(0.5, 1.08, 'Security Risk Assessment Matrix', 
            transform=ax.transAxes, ha='center', fontsize=18, 
            fontweight='bold', color='#1a1a1a')
    ax.text(0.5, 1.03, 'Zero vulnerabilities across all severity levels', 
            transform=ax.transAxes, ha='center', fontsize=12, color='#666666')
    
    ax.text(0.5, -0.15, 'Overall Risk Level: 🟢 MINIMAL  |  95.65% Safe/Secure', 
            transform=ax.transAxes, ha='center', fontsize=13, 
            fontweight='bold', color=BRAND_COLOR,
            bbox=dict(boxstyle='round,pad=0.6', facecolor='#e8f5e9', 
                     edgecolor=BRAND_COLOR, linewidth=2))
    
    return save_chart('risk_assessment.png', 'Risk Assessment')

def create_gas_optimization():
    print("Creating Chart 5/7: Gas Optimization...")
    
    fig, ax = plt.subplots(figsize=(12, 9), facecolor='white')
    
    operations = ['transfer()', 'approve()', 'transferFrom()', 
                  'Error\\nHandling', 'Unchecked\\nArithmetic']
    savings = [4.1, 3.2, 3.9, 90, 67.6]
    colors = ['#88cc00', '#88cc00', '#88cc00', BRAND_COLOR, BRAND_COLOR]
    
    x_pos = np.arange(len(operations))
    bars = ax.bar(x_pos, savings, color=colors, edgecolor='white', 
                  linewidth=2, width=0.7)
    
    bars[3].set_edgecolor('#ff8800')
    bars[3].set_linewidth(4)
    bars[4].set_edgecolor('#4488ff')
    bars[4].set_linewidth(3)
    
    for bar, val in zip(bars, savings):
        height = bar.get_height()
        ax.text(bar.get_x() + bar.get_width()/2, height + 2,
                f'-{val}%', ha='center', va='bottom',
                fontsize=13, fontweight='bold', color='#333333')
    
    ax.axhline(y=12, color='#ff8800', linestyle='--', linewidth=2, alpha=0.7)
    ax.text(len(operations) - 0.5, 14, 'Average: 12% savings', 
            ha='right', fontsize=11, fontweight='bold', color='#ff8800',
            bbox=dict(boxstyle='round,pad=0.4', facecolor='#fff3e0', 
                     edgecolor='#ff8800', linewidth=1.5))
    
    ax.set_xticks(x_pos)
    ax.set_xticklabels(operations, fontsize=12, fontweight='bold')
    ax.set_ylabel('Gas Savings (%)', fontsize=12, fontweight='bold', 
                  color='#333333')
    ax.set_ylim(0, 100)
    
    ax.grid(axis='y', alpha=0.3, linestyle='--', linewidth=0.5)
    ax.set_axisbelow(True)
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    
    ax.text(0.5, 1.08, 'Gas Optimization Analysis', 
            transform=ax.transAxes, ha='center', fontsize=18, 
            fontweight='bold', color='#1a1a1a')
    ax.text(0.5, 1.03, 'Score: 97/100 - Professional Grade', 
            transform=ax.transAxes, ha='center', fontsize=12, color='#666666')
    
    note_text = '⚡ Custom errors save 90% gas compared to traditional require statements'
    ax.text(0.5, -0.15, note_text, 
            transform=ax.transAxes, ha='center', fontsize=11, 
            fontweight='bold', color=BRAND_COLOR,
            bbox=dict(boxstyle='round,pad=0.5', facecolor='#e8f5e9', 
                     edgecolor=BRAND_COLOR, linewidth=2))
    
    return save_chart('gas_optimization.png', 'Gas Optimization')

def create_code_quality_profile():
    print("Creating Chart 6/7: Code Quality Profile...")
    
    fig, ax = plt.subplots(figsize=(10, 10), 
                          subplot_kw=dict(projection='polar'), 
                          facecolor='white')
    
    categories = ['Code\\nMaintainability', 'Security\\nHotspots', 
                  'Documentation', 'Test\\nCoverage', 'Code\\nComplexity', 
                  'Code\\nDuplication', 'Technical\\nDebt', 
                  'Standards\\nCompliance']
    values = [98, 100, 100, 95, 92, 100, 100, 100]
    
    num_vars = len(categories)
    angles = np.linspace(0, 2 * np.pi, num_vars, endpoint=False).tolist()
    values += values[:1]
    angles += angles[:1]
    
    ax.plot(angles, values, 'o-', linewidth=3, color=BRAND_COLOR, markersize=10, 
            markerfacecolor=BRAND_COLOR, markeredgecolor='white', 
            markeredgewidth=2)
    ax.fill(angles, values, alpha=0.25, color=BRAND_COLOR)
    
    ax.set_xticks(angles[:-1])
    ax.set_xticklabels(categories, fontsize=11, fontweight='bold')
    ax.set_ylim(0, 100)
    ax.set_yticks([20, 40, 60, 80, 100])
    ax.set_yticklabels(['20', '40', '60', '80', '100'], fontsize=10, 
                       color='#666666')
    
    ax.spines['polar'].set_color('#cccccc')
    ax.spines['polar'].set_linewidth(1.5)
    ax.grid(color='#cccccc', linestyle='--', linewidth=0.8, alpha=0.5)
    
    ax.text(0, 120, 'Code Quality Profile', ha='center', fontsize=18, 
            fontweight='bold', color='#1a1a1a', transform=ax.transData)
    ax.text(0, 112, 'Multi-Dimensional Assessment - Score: 97/100', 
            ha='center', fontsize=12, color='#666666', transform=ax.transData)
    
    for angle, value, label in zip(angles[:-1], values[:-1], categories):
        if value == 100:
            ax.plot([angle, angle], [0, value], color='#ffd700', 
                   linewidth=2, alpha=0.5, linestyle='--')
    
    legend_text = '★ Perfect Score (100/100)'
    ax.text(np.pi, -20, legend_text, ha='center', fontsize=10, 
            color='#ffd700', fontweight='bold', transform=ax.transData,
            bbox=dict(boxstyle='round,pad=0.4', facecolor='#fffef0', 
                     edgecolor='#ffd700', linewidth=1.5))
    
    return save_chart('code_quality_profile.png', 'Code Quality Profile')

def create_vulnerability_scan():
    print("Creating Chart 7/7: Vulnerability Scan...")
    
    fig, ax = plt.subplots(figsize=(14, 11), facecolor='white')
    ax.axis('off')
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 18)
    
    ax.text(5, 17.2, 'Security Vulnerability Assessment', 
            ha='center', fontsize=20, fontweight='bold', color='#1a1a1a')
    ax.text(5, 16.6, 'Score: 98/100 - Exceptional Security', 
            ha='center', fontsize=13, color='#666666')
    
    vulnerabilities = [
        'Reentrancy Attack - Protected',
        'Integer Overflow/Underflow - Protected',
        'Unchecked Call Return - Safe',
        'Access Control Flaws - None Found',
        'Front-Running - Resistant',
        'Timestamp Dependency - N/A',
        'Delegatecall Injection - N/A',
        'Hidden Backdoor - None',
        'Proxy Pattern Risks - Direct Implementation',
        'Mint/Burn Exploits - None',
        'Centralization Risk - Zero (Fully Decentralized)',
        'Gas Limit DoS - Protected',
        'Transaction Ordering - Resistant',
        'Arithmetic Issues - Protected',
        'Logic Errors - None'
    ]
    
    y_start = 15.2
    y_step = 0.85
    
    for i, vuln in enumerate(vulnerabilities):
        y = y_start - (i * y_step)
        
        if i % 2 == 0:
            bg_color = '#f5f5f5'
        else:
            bg_color = 'white'
        
        rect = mpatches.FancyBboxPatch((0.5, y - 0.35), 9, 0.7,
                                       boxstyle="round,pad=0.05",
                                       facecolor=bg_color, edgecolor='#e0e0e0',
                                       linewidth=1)
        ax.add_patch(rect)
        
        ax.text(0.8, y, '✅', ha='left', va='center', 
                fontsize=18, color=BRAND_COLOR, fontweight='bold')
        
        ax.text(1.5, y, vuln, ha='left', va='center', 
                fontsize=11, color='#333333')
    
    summary_y = y_start - (len(vulnerabilities) * y_step) - 0.5
    ax.text(5, summary_y, '🛡️ Zero Vulnerabilities Identified  |  15/15 Checks Passed', 
            ha='center', fontsize=13, fontweight='bold', color=BRAND_COLOR,
            bbox=dict(boxstyle='round,pad=0.6', facecolor='#e8f5e9', 
                     edgecolor=BRAND_COLOR, linewidth=2.5))
    
    score_badge_y = summary_y - 0.9
    ax.text(5, score_badge_y, '98/100 Security Features Score', 
            ha='center', fontsize=12, fontweight='bold', color='white',
            bbox=dict(boxstyle='round,pad=0.5', facecolor=BRAND_COLOR, 
                     edgecolor='#00aa33', linewidth=2))
    
    return save_chart('vulnerability_scan.png', 'Vulnerability Scan')

def main():
    print("="*60)
    print("ROUM Token - CertiK Audit Charts Generator")
    print("="*60)
    print()
    
    ensure_charts_directory()
    print()
    
    generated_charts = []
    generated_charts.append(create_security_score_gauge())
    generated_charts.append(create_industry_comparison())
    generated_charts.append(create_test_results())
    generated_charts.append(create_risk_assessment())
    generated_charts.append(create_gas_optimization())
    generated_charts.append(create_code_quality_profile())
    generated_charts.append(create_vulnerability_scan())
    
    print()
    print("="*60)
    print(f"✅ ALL {len(generated_charts)} CHARTS CREATED SUCCESSFULLY!")
    print(f"Location: {CHARTS_DIR}/")
    print("="*60)
    print()
    print("Charts generated:")
    for i, chart in enumerate(generated_charts, 1):
        print(f"{i}. {chart}")
    print()
    print("Next step: Update docs/CERTIK-AUDIT-VISUAL.md with new image paths")

if __name__ == "__main__":
    main()