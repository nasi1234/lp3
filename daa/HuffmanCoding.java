import java.util.Comparator;
import java.util.PriorityQueue;

class Node {
    char ch;
    int freq;
    Node left, right;

    Node(char ch, int freq) {
        this.ch = ch;
        this.freq = freq;
        this.left = null;
        this.right = null;
    }
}

class NodeComparator implements Comparator<Node> {
    @Override
    public int compare(Node a, Node b) {
        return a.freq - b.freq;
    }
}

class HuffmanCoding {

    static void generateCodes(Node root, String code, StringBuilder result) {
        if (root == null) return;

        if (root.left == null && root.right == null) {
            result.append(root.ch)
                  .append(":")
                  .append(code)
                  .append("\n");
        }

        generateCodes(root.left, code + "0", result);
        generateCodes(root.right, code + "1", result);
    }

    public static void huffmanEncode(char[] chars, int[] freqs) {
        PriorityQueue<Node> pq = new PriorityQueue<>(new NodeComparator());

        for (int i = 0; i < chars.length; i++) {
            pq.add(new Node(chars[i], freqs[i]));
        }

        while (pq.size() > 1) {
            Node left = pq.poll();
            Node right = pq.poll();

            Node newNode = new Node('-', left.freq + right.freq);
            newNode.left = left;
            newNode.right = right;

            pq.add(newNode);
        }

        Node root = pq.poll();
        StringBuilder result = new StringBuilder();
        generateCodes(root, "", result);

        System.out.println(result.toString());
    }

    public static void main(String[] args) {
        char[] chars = { 'a', 'b', 'c', 'd', 'e', 'f' };
        int[] freqs = { 5, 9, 12, 13, 16, 45 };

        System.out.println("Huffman Codes:");
        huffmanEncode(chars, freqs);
    }
}
