# Mẫu báo cáo thực tập tốt nghiệp LaTeX

[![LaTeX PDF and release](https://github.com/Ex6TenZ13/LaTeX-TTTN/actions/workflows/latex-release.yml/badge.svg?branch=main)](https://github.com/Ex6TenZ13/LaTeX-TTTN/actions/workflows/latex-release.yml)

[English version](#english)

> 📣 **Mẫu LaTeX TTTN đang trong quá trình chỉnh sửa và hoàn thiện**
>
> Nội dung, cấu trúc và định dạng trong các tệp `.tex` có thể thay đổi; PDF và ảnh xem trước sẽ được cập nhật theo. Nếu đang sử dụng mẫu, hãy kiểm tra [bản phát hành mới nhất](https://github.com/Ex6TenZ13/LaTeX-TTTN/releases/latest) trước khi bắt đầu hoặc tiếp tục báo cáo.
>
> Có ý tưởng hoặc phát hiện lỗi? Hãy gửi góp ý tại [Issues](https://github.com/Ex6TenZ13/LaTeX-TTTN/issues). Vui lòng nêu tệp hoặc phần liên quan, đề xuất hoặc vấn đề, và ảnh minh họa nếu phù hợp.

[![Trang đầu của báo cáo](https://github.com/Ex6TenZ13/LaTeX-TTTN/blob/release-preview/Bao_cao_TTTN.png?raw=true)](https://github.com/Ex6TenZ13/LaTeX-TTTN/blob/release-preview/Bao_cao_TTTN.pdf)

Bấm vào ảnh để xem PDF mẫu báo cáo và các quy định về hình thức, cách trình bày báo cáo bằng LaTeX.

**[Xem PDF mới nhất](https://github.com/Ex6TenZ13/LaTeX-TTTN/blob/release-preview/Bao_cao_TTTN.pdf)** · **[Tải ZIP](https://github.com/Ex6TenZ13/LaTeX-TTTN/releases/latest/download/LaTeX-TTTN.zip)** · [Tất cả bản phát hành](https://github.com/Ex6TenZ13/LaTeX-TTTN/releases)

## Tải và sử dụng gói ZIP

1. Tải [gói ZIP của bản phát hành mới nhất](https://github.com/Ex6TenZ13/LaTeX-TTTN/releases/latest/download/LaTeX-TTTN.zip) từ mục **Assets** trong trang Releases.
2. Giải nén ZIP vào một thư mục trên máy tính; không mở hoặc biên dịch tệp `.tex` trực tiếp bên trong ZIP. Giữ nguyên cấu trúc thư mục, đặc biệt là thư mục `figures`.
3. Mở TeXstudio, dùng **File → Open** để đi tới thư mục vừa giải nén và mở `Bao_cao_TTTN.tex`. TeXstudio sẽ hiển thị các tệp cùng thư mục trong **File Explorer**; chọn **Build & View** hoặc nhấn `F5` để biên dịch và xem PDF.

Gói ZIP chứa mã nguồn và tài nguyên của mẫu, không phải file PDF đã biên dịch. Nếu TeXstudio/MiKTeX hỏi cài package còn thiếu, hãy cho phép cài đặt rồi biên dịch lại.

## Cài đặt trên Windows

### 1. MiKTeX

1. Tải **Basic MiKTeX Installer** từ [trang cài đặt chính thức](https://miktex.org/howto/install-miktex).
2. Cài đặt cho người dùng hiện tại, chọn khổ giấy **A4** và cho phép MiKTeX tự động cài các gói còn thiếu.
3. Mở **MiKTeX Console**, vào **Updates** và cài toàn bộ bản cập nhật trước khi biên dịch tài liệu.

### 2. TeXstudio

1. Tải và cài [TeXstudio](https://texstudio.org/).
2. Mở tệp `Bao_cao_TTTN.tex`.
3. Vào **Options → Configure TeXstudio → Build**, chọn **PdfLaTeX** làm trình biên dịch mặc định.
4. Nhấn **Build & View** hoặc phím `F5` để biên dịch và xem PDF.

### 3. SumatraPDF

Tải và cài [SumatraPDF](https://www.sumatrapdfreader.org/download-free-pdf-viewer), sau đó vào **Options → Configure TeXstudio → Commands → External PDF Viewer** và nhập:

```text
"C:/Program Files/SumatraPDF/SumatraPDF.exe" -reuse-instance -forward-search "?c:am.tex" @ "?am.pdf"
```

Nếu SumatraPDF được cài ở thư mục khác, hãy sửa đường dẫn trong lệnh trên. Để tìm ngược từ PDF về mã nguồn, mở **Settings → Options** trong SumatraPDF và đặt lệnh inverse search theo [hướng dẫn tích hợp LaTeX](https://www.sumatrapdfreader.org/docs/LaTeX-integration):

```text
"C:\Program Files\TeXstudio\texstudio.exe" "%f" -line %l
```
---

## English

### Update notice

> 📣 **The LaTeX-TTTN template is being revised and finalized.**
>
> The content, structure, and formatting of the `.tex` files may change. The PDF and preview image will be updated accordingly. If you are using this template, check the [latest release](https://github.com/Ex6TenZ13/LaTeX-TTTN/releases/latest) before starting or continuing your report.
>
> Have an idea or found an issue? Please share it via [Issues](https://github.com/Ex6TenZ13/LaTeX-TTTN/issues). Include the relevant file or section, your suggestion or a description of the problem, and a screenshot if helpful.

### PDF preview and releases

Click the image to view a sample report PDF and the guidelines for report formatting and presentation in LaTeX.

**[View the latest PDF](https://github.com/Ex6TenZ13/LaTeX-TTTN/blob/release-preview/Bao_cao_TTTN.pdf)** · **[Download the ZIP](https://github.com/Ex6TenZ13/LaTeX-TTTN/releases/latest/download/LaTeX-TTTN.zip)** · [All releases](https://github.com/Ex6TenZ13/LaTeX-TTTN/releases)

### Download and use the ZIP package

1. Download the [latest ZIP package](https://github.com/Ex6TenZ13/LaTeX-TTTN/releases/latest/download/LaTeX-TTTN.zip) from the **Assets** section of the Releases page.
2. Extract the ZIP archive to a folder on your computer. Do not open or compile the `.tex` file directly from inside the archive. Keep the folder structure intact, especially the `figures` folder.
3. In TeXstudio, choose **File → Open**, navigate to the extracted folder, and open `Bao_cao_TTTN.tex`. TeXstudio's **File Explorer** shows the other files in the same folder. Select **Build & View** or press `F5` to compile the document and view the PDF.

The ZIP package contains the template's source files and resources, not the compiled PDF. If TeXstudio/MiKTeX asks to install missing packages, allow the installation and compile again. The archive contains only `Bao_cao_TTTN.tex`, `References.bib`, `Regulations.tex`, and the files in `figures/`.

### Installing on Windows

#### 1. MiKTeX

1. Download the **Basic MiKTeX Installer** from the [official installation page](https://miktex.org/howto/install-miktex).
2. Install it for the current user, select **A4** paper, and allow MiKTeX to install missing packages automatically.
3. Open **MiKTeX Console**, go to **Updates**, and install all updates before compiling.

#### 2. TeXstudio

1. Download and install [TeXstudio](https://texstudio.org/).
2. Open `Bao_cao_TTTN.tex`.
3. Go to **Options → Configure TeXstudio → Build** and select **PdfLaTeX** as the default compiler.
4. Select **Build & View** or press `F5` to compile and view the PDF.

#### 3. SumatraPDF

Download and install [SumatraPDF](https://www.sumatrapdfreader.org/download-free-pdf-viewer). In TeXstudio, go to **Options → Configure TeXstudio → Commands → External PDF Viewer** and enter:

```text
"C:/Program Files/SumatraPDF/SumatraPDF.exe" -reuse-instance -forward-search "?c:am.tex" @ "?am.pdf"
```

If SumatraPDF is installed in a different folder, update the path in the command. To jump from the PDF back to the source, open **Settings → Options** in SumatraPDF and set the inverse-search command following the [LaTeX integration guide](https://www.sumatrapdfreader.org/docs/LaTeX-integration):

```text
"C:\Program Files\TeXstudio\texstudio.exe" "%f" -line %l
```
