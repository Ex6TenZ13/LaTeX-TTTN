# Mẫu báo cáo thực tập tốt nghiệp LaTeX

[![LaTeX PDF and release](https://github.com/Ex6TenZ13/LaTeX-TTTN/actions/workflows/latex-release.yml/badge.svg?branch=main)](https://github.com/Ex6TenZ13/LaTeX-TTTN/actions/workflows/latex-release.yml)

[![Trang đầu của báo cáo](https://github.com/Ex6TenZ13/LaTeX-TTTN/blob/release-preview/Bao_cao_TTTN.png?raw=true)](https://github.com/Ex6TenZ13/LaTeX-TTTN/releases/latest/download/Bao_cao_TTTN.pdf)

**[Tải PDF mới nhất](https://github.com/Ex6TenZ13/LaTeX-TTTN/releases/latest/download/Bao_cao_TTTN.pdf)** · **[Tải mã nguồn ZIP](https://github.com/Ex6TenZ13/LaTeX-TTTN/releases/latest/download/LaTeX-TTTN-source.zip)** · [Tất cả bản phát hành](https://github.com/Ex6TenZ13/LaTeX-TTTN/releases)

Ảnh được tạo từ **trang 1** của PDF. Mẫu hiện đặt `Regulations.tex` trước trang bìa, nên ảnh là trang quy định. Sau mỗi lần phát hành chính thức, workflow tải PDF của release mới nhất để cập nhật ảnh trên nhánh `release-preview`; không commit PDF hoặc ảnh tự động vào `main`.

Trước release chính thức đầu tiên, ảnh là bản xem trước khởi tạo từ mã nguồn; các liên kết `releases/latest` chỉ hoạt động sau khi bạn **Publish** một release không phải prerelease. Xem [thông tin ảnh](https://github.com/Ex6TenZ13/LaTeX-TTTN/blob/release-preview/release.json). Repository là private: người xem cần đăng nhập và có quyền truy cập.

## Trình biên dịch

Dùng **pdfLaTeX** qua `latexmk`. Mẫu dùng `inputenc`, font encoding `T1`, `babel` tiếng Anh, `tgtermes` và `mathptmx`; không dùng `fontspec` hay phông hệ thống cần XeLaTeX. `latexmk` tự chạy lại để cập nhật mục lục và tham chiếu.

```bash
latexmk -norc -pdf -no-shell-escape -interaction=nonstopmode \
  -halt-on-error -file-line-error Bao_cao_TTTN.tex
```

Máy cá nhân cần TeX Live/MacTeX có các gói được mẫu sử dụng. Workflow cài các nhóm gói tương ứng trên Ubuntu 24.04. `References.bib` hiện chưa có trong repository, nên phần thư mục tài liệu tham khảo chỉ được gọi nếu file đó tồn tại. Nếu sau này bổ sung file `.bib`, cần cập nhật danh sách đóng gói để ZIP vẫn biên dịch được độc lập.

## Kiểm tra mà không phát hành

Push vào `main` hoặc mở pull request vào `main` sẽ chạy **LaTeX PDF and release**. Bạn cũng có thể vào **Actions → LaTeX PDF and release → Run workflow**, chọn `main`, để `refresh_preview` tắt.

Một lần chạy thành công có artifact `report-<commit>` chứa:

- `Bao_cao_TTTN.pdf`: báo cáo đã biên dịch.
- `Bao_cao_TTTN.png`: ảnh trang đầu.
- `LaTeX-TTTN-source.zip`: gói nguồn đã kiểm tra từng file với nội dung trong commit.

Artifacts được giữ 14 ngày; assets của release không có giới hạn lưu 14 ngày này. Nếu biên dịch lỗi, xem bước **Build the report** và artifact chẩn đoán (giữ 7 ngày).

## Tạo release bằng tag

Sau khi thay đổi workflow đã có trên `main` và CI thành công, tạo một tag `v*` mới trên commit thuộc lịch sử `main`. Ví dụ:

```bash
git switch main
git pull --ff-only
git tag -a v1.0.0 -m "LaTeX TTTN v1.0.0"
git push origin v1.0.0
```

Workflow biên dịch đúng commit của tag và tạo **draft release** với đúng hai file đính kèm:

1. `Bao_cao_TTTN.pdf`
2. `LaTeX-TTTN-source.zip`

Vào **Releases → draft của tag**, tải và kiểm tra cả hai file, sau đó bấm **Publish release**. Chọn release ổn định, không đánh dấu prerelease; đặt làm **Latest** nếu GitHub hiển thị tùy chọn này. Việc publish được thực hiện bằng tài khoản của bạn để sự kiện `release: published` kích hoạt bước cập nhật ảnh.

Workflow **không tự publish**, không tự tạo tag và không ghi đè assets của release đã publish. Nếu chạy lại một tag còn là draft, hai assets được cập nhật. GitHub có thể hiển thị thêm hai liên kết **Source code (zip/tar.gz)** tự sinh; chúng là snapshot toàn repository, khác với gói nguồn chọn lọc đính kèm ở trên.

## Nội dung gói nguồn

```text
.gitignore
Bao_cao_TTTN.tex
Regulations.tex
figures/
  fit.jpg
  tnut.jpg
```

Gói ZIP lấy từ Git commit, chỉ chọn ba file ở gốc và mọi file đã commit trong `figures/`. Không chứa `.git`, README, workflow, PDF, ảnh preview hoặc file tạm chưa commit. Script kiểm tra danh sách file, nội dung từng byte và CRC; không chỉ kiểm tra phần mở rộng.

**ZIP được dùng theo lựa chọn của chủ repository thay cho RAR.** Không có ZIP đổi đuôi thành `.rar`. [Giấy phép RARLAB](https://www.rarlab.com/license.htm) giới hạn dùng thử ở 40 ngày; việc chạy RAR thường xuyên cần giấy phép phù hợp. Workflow không cài RAR và không cần secret giấy phép.

## Giới hạn README và cách xác minh

GitHub README không hỗ trợ nhúng trình đọc PDF bằng `iframe`, `object` hoặc `embed`. Vì vậy README dùng PNG có liên kết tải PDF; GitHub có trình xem riêng cho file PDF trong repository, nhưng đó không phải trình đọc nhúng trong Markdown. [Cách GitHub xử lý markup](https://github.com/github/markup), [ảnh trong Markdown](https://docs.github.com/en/get-started/writing-on-github/getting-started-with-writing-and-formatting-on-github/basic-writing-and-formatting-syntax#images).

Các đường dẫn tải dùng tên asset cố định theo [cú pháp latest release của GitHub](https://docs.github.com/en/repositories/releasing-projects-on-github/linking-to-releases). Không cần sửa README khi tăng phiên bản.

Sau khi publish:

1. Kiểm tra lần chạy **LaTeX PDF and release** do sự kiện `release` có bước **update-preview** màu xanh.
2. Kiểm tra release có PDF và ZIP, giải nén ZIP để đối chiếu danh sách trên.
3. Mở README, kiểm tra ảnh và bấm ảnh để tải PDF của release mới nhất.
4. Kiểm tra `release-preview/release.json` có đúng tag của release mới nhất. `main` không nhận commit tự động.

Ảnh có thể cập nhật chậm hơn release trong thời gian workflow chạy hoặc do bộ nhớ đệm của GitHub. Nếu thay đổi release được chọn làm Latest, hoặc cần khôi phục sau lỗi, chạy **Run workflow** trên `main` và bật `refresh_preview`. Chế độ này chỉ đọc release đã publish để cập nhật ảnh, không tạo release mới.

Workflow dùng `GITHUB_TOKEN`: build chỉ cần `contents: read`; tạo draft và cập nhật nhánh ảnh cần `contents: write`. Nhánh `release-preview` cần cho phép GitHub Actions push. Nếu repository áp dụng quy tắc phê duyệt bổ sung, hoàn tất phê duyệt đó trên GitHub; không bỏ qua các quy tắc. Cơ chế draft + Publish thủ công hoạt động mà không phụ thuộc vào tính năng required reviewers cho environment của gói GitHub.
