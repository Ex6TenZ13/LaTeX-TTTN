# Mẫu báo cáo thực tập tốt nghiệp LaTeX

[![LaTeX PDF and release](https://github.com/Ex6TenZ13/LaTeX-TTTN/actions/workflows/latex-release.yml/badge.svg?branch=main)](https://github.com/Ex6TenZ13/LaTeX-TTTN/actions/workflows/latex-release.yml)

> 📣 **Mẫu LaTeX TTTN đang trong quá trình chỉnh sửa và hoàn thiện**
>
> Nội dung, cấu trúc và định dạng trong các tệp `.tex` có thể thay đổi; PDF và ảnh xem trước sẽ được cập nhật theo. Nếu đang sử dụng mẫu, hãy kiểm tra [bản phát hành mới nhất](https://github.com/Ex6TenZ13/LaTeX-TTTN/releases/latest) trước khi bắt đầu hoặc tiếp tục báo cáo.
>
> Có ý tưởng hoặc phát hiện lỗi? Hãy gửi góp ý tại [Issues](https://github.com/Ex6TenZ13/LaTeX-TTTN/issues). Vui lòng nêu tệp hoặc phần liên quan, đề xuất hoặc vấn đề, và ảnh minh họa nếu phù hợp.

[![Trang đầu của báo cáo](https://github.com/Ex6TenZ13/LaTeX-TTTN/blob/release-preview/Bao_cao_TTTN.png?raw=true)](https://github.com/Ex6TenZ13/LaTeX-TTTN/blob/release-preview/Bao_cao_TTTN.pdf)

Bấm ảnh để xem PDF trong trình duyệt. Mở tab mới: giữ **⌘** khi bấm trên Mac, **Ctrl** trên Windows/Linux, hoặc chọn **Open Link in New Tab** trong menu chuột phải.

**[Tải PDF mới nhất](https://github.com/Ex6TenZ13/LaTeX-TTTN/releases/latest/download/Bao_cao_TTTN.pdf)** · **[Tải mã nguồn ZIP](https://github.com/Ex6TenZ13/LaTeX-TTTN/releases/latest/download/LaTeX-TTTN-source.zip)** · [Tất cả bản phát hành](https://github.com/Ex6TenZ13/LaTeX-TTTN/releases)

## Tải và sử dụng gói ZIP

1. Tải [gói ZIP mã nguồn của bản phát hành mới nhất](https://github.com/Ex6TenZ13/LaTeX-TTTN/releases/latest/download/LaTeX-TTTN-source.zip) từ mục **Assets** trong trang Releases.
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
