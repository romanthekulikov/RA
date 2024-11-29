import java.io.*;
import java.nio.ByteBuffer;
import java.nio.charset.StandardCharsets;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.Objects;
import java.util.stream.Collectors;

public class Main {
    private static final String ERROR_FILE_READ_EX = "Файл не найден или поврежден";
    private static final String ERROR_FILE_OPEN_EX = "Не удалось создать или открыть файл";

    public static void main(String[] args) {
        clearOutputFile();
        List<String> lines = getFileLines(args[1]);
        for (String line : lines) {
            try {
                if (line.startsWith("//") || line.isEmpty()) {
                    continue;
                }
                String[] arguments = line.toLowerCase().trim().replaceAll("\\s+", " ").split(" ");
                List<String> argumentsList = new ArrayList<>(Arrays.asList(arguments));
                int i = 0;
                String expectedTriangleType = argumentsList.get(i);
                int requiredArgumentsLength = 4;
                if (Objects.equals(expectedTriangleType, "не") || Objects.equals(expectedTriangleType, "неизвестная")) {
                    argumentsList.set(0, expectedTriangleType + " " + argumentsList.get(1));
                    argumentsList.remove(1);
                }
                expectedTriangleType = argumentsList.get(0);
                if (argumentsList.size() < requiredArgumentsLength) {
                    for (int k = argumentsList.size(); k <= 4; k++) {
                        argumentsList.add("-1");
                    }
                } else if (argumentsList.size() > requiredArgumentsLength) {
                    writeResultToFile(expectedTriangleType.equals("неизместная ошибка"));
                    continue;
                }
                String firstTriangleSide = argumentsList.get(1);
                String secondTriangleSide = argumentsList.get(2);
                String thirdTriangleSide = argumentsList.get(3);



                String executableProgram = args[0];
                ProcessBuilder builder = new ProcessBuilder(executableProgram, firstTriangleSide, secondTriangleSide, thirdTriangleSide);
                Process process = builder.start();
                try (BufferedReader br = new BufferedReader(new InputStreamReader(process.getInputStream()))) {
                    long time1 = System.currentTimeMillis();
                    String response = br.readLine();
                    long time2 = System.currentTimeMillis();
                    System.out.println(time2 - time1);
                    if (response != null) {
                        writeResultToFile(response.equals(expectedTriangleType));
                    }
                }
            } catch (Exception exception) {
                writeResultToFile(false);
            }
        }
    }

    static void clearOutputFile() {
        try (FileWriter writer = new FileWriter("test_result.txt", false))
        {
            writer.write("");
        } catch (IOException e) {
            throw new RuntimeException(ERROR_FILE_OPEN_EX);
        }
    }

    static List<String> getFileLines(String fileDir) {
        List<String> lines = new ArrayList<>();
        try {
            BufferedReader reader = new BufferedReader(new FileReader(fileDir));
            String line;
            while ((line = reader.readLine()) != null) {
                lines.add(line);
            }
        } catch (Exception exception) {
            throw new IllegalArgumentException(ERROR_FILE_READ_EX);
        }

        return lines;
    }

    static void writeResultToFile(Boolean success) {
        try (FileWriter writer = new FileWriter("test_result.txt", true)) {
            if (success) {
                writer.write("success\n");
            } else {
                writer.write("error\n");
            }
        } catch (IOException e) {
            System.out.println(ERROR_FILE_OPEN_EX);
        }
    }
}