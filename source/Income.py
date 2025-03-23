#Copyright (c) 2025 @sarlakmohammad
    #All rights reserved

import matplotlib.pyplot as plt

def open_income_page(items:list):
    # Sample data
    y = []
    x = []
    for i in range(1, 13):
        x.append(i)
        y.append(0)

    for item in items:
        _index = item[0] - 1
        y.pop(_index)
        y.insert(_index,item[1])

    # Create a line chart
    plt.figure(figsize=(20, 10))
    plt.plot(x, y,
             marker='o',
             linestyle='-',
             color='green',
             linewidth=3,
             markersize=12,
             markerfacecolor='#00FF00'
             )

    # setting x and y-axis range
    plt.ylim(-50, 250)
    plt.xlim(0, 13)

    # Add annotations
    for i, (xi, yi) in enumerate(zip(x, y)):
        plt.annotate(f'{yi}', (xi, yi), textcoords="offset points", xytext=(0, 10), ha='center', size=20)

    # Add title and labels
    plt.title('reporting the income per month', size=30, pad=33)
    plt.xlabel('month', size=30, labelpad=10)
    plt.ylabel('income (million tooman)', size=30, labelpad=30)

    # Display grid
    plt.grid(True)

    # creating file
    plt.savefig('image/chart')

    # show
    plt.show()