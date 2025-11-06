import java.util.Arrays;

class Item {
    int value, weight;

    Item(int value, int weight) {
        this.value = value;
        this.weight = weight;
    }
}

class FractionalKnapsack {

    static double getMaxValue(Item[] items, int capacity) {
        Arrays.sort(items, (Item a, Item b) -> {
            double r1 = (double) a.value / a.weight;
            double r2 = (double) b.value / b.weight;
            if (r1 < r2) return 1;
            else if (r1 > r2) return -1;
            else return 0;
        });

        int curWeight = 0;
        double finalValue = 0.0;

        for (Item item : items) {
            if (curWeight + item.weight <= capacity) {
                curWeight += item.weight;
                finalValue += item.value;
            } else {
                int remain = capacity - curWeight;
                finalValue += item.value * ((double) remain / item.weight);
                break;
            }
        }

        return finalValue;
    }

    public static void main(String[] args) {
        int capacity = 50;
        Item[] items = {
            new Item(60, 10),
            new Item(100, 20),
            new Item(120, 30)
        };

        double maxValue = getMaxValue(items, capacity);
        System.out.println("Maximum value in Knapsack = " + maxValue);
    }
}