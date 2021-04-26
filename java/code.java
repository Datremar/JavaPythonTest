public class Main {
    public static void main(String[] args) {
      int n = Integer.parseInt(args[0]);
        int[] arr = new int[n]; // lolz

        for (int i = 1; i <= n; i++) {
            arr[i - 1] = i * i;
        }

        for (int i = 1; i <= n; i++) {
            System.out.println(arr[i - 1]);
        }
    }
}
