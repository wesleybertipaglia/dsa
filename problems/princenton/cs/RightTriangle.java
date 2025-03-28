public class RightTriangle {
    public static void main(String[] args) {
        if (args.length < 3) {
            System.out.println("Uso: java Assignments.RightTriangle <n1> <n2> <n3>");
            return;
        }

        int n1 = Integer.parseInt(args[0]);
        int n2 = Integer.parseInt(args[1]);
        int n3 = Integer.parseInt(args[2]);

        if (n1 <= 0 || n2 <= 0 || n3 <= 0) {
            System.out.println(false);
            return;
        }

        int a = Math.min(n1, Math.min(n2, n3));
        int b = n1 + n2 + n3 - a - Math.max(n1, Math.max(n2, n3));
        int c = Math.max(n1, Math.max(n2, n3));

        boolean result = (a * a + b * b == c * c);
        System.out.println(result);
    }
}
