import matplotlib.pyplot as plt
import numpy
def read_data(filename):
    data = []
    with open(filename, 'r') as f:
        for line in f.readlines():
            if not line.startswith('#'): # If 'line' is not a header
                data.append([int(word) for word in line.split(',')])
    return data

if __name__ == '__main__':
    # Load score data
    class_kr = read_data('data/class_score_kr.csv')
    class_en = read_data('data/class_score_en.csv')

    # TODO) Prepare midterm, final, and total scores
    midterm_kr, final_kr = zip(*class_kr)
    total_kr = [40/125*midterm + 60/100*final for (midterm, final) in class_kr]
    print(total_kr)
    midterm_en, final_en = zip(*class_en)
    total_en = [40/125*midterm + 60/100*final for (midterm, final) in class_en]

    # TODO) Plot midterm/final scores as points
    plt.figure(figsize=(8, 10))
    plt.subplot(2, 1, 1)
    plt.scatter(midterm_kr, final_kr, marker='o', color='red', label='Data points')
    plt.scatter(midterm_en, final_en, marker='+', color='blue', label='Data points')
    plt.xlabel('Midterm scores')
    plt.ylabel('Final scores')
    plt.xlim([0, 125])
    plt.ylim([0, 100])
    plt.legend()
    plt.grid()
    # TODO) Plot total scores as a histogram
    plt.subplot(2, 1, 2)
    plt.hist(total_en, bins=numpy.arange(0,101,5), color='blue', alpha=0.5, label='English')
    plt.hist(total_kr, bins=numpy.arange(0,101,5), color='red', alpha=0.5, label='Korean')
    plt.xlabel('Total scores')
    plt.ylabel('The number of students')
    plt.yticks(range(0, 9, 1))
    plt.legend(loc='upper left')
    plt.xlim([0, 100])
    plt.tight_layout()
    plt.show()