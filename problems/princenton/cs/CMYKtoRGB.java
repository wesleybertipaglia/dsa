public class CMYKtoRGB {
    public static void main(String[] args) {
        if (args.length < 4) {
            System.out.println("Uso: java Assignments.CMYKtoRGB <cyan> <magenta> <yellow> <black>");
            return;
        }

        double cyan = Double.parseDouble(args[0]);
        double magenta = Double.parseDouble(args[1]);
        double yellow = Double.parseDouble(args[2]);
        double black = Double.parseDouble(args[3]);

        int red = (int) Math.round(255 * (1 - cyan) * (1 - black));
        int green = (int) Math.round(255 * (1 - magenta) * (1 - black));
        int blue = (int) Math.round(255 * (1 - yellow) * (1 - black));

        System.out.printf("RGB: %d %d %d%n", red, green, blue);
    }
}
