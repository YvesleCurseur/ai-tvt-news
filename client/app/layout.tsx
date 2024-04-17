import "./globals.css";

export const metadata = {
  title: "AI TVT Actualités",
  description: "Assistant IA qui écrit les News de la chaîne Youtube TVT.",
};

export default function RootLayout({
  children,
}: {
  children: React.ReactNode;
}) {
  return (
    <html lang="en">
      {/* Make the background code Green to Yellow */}
      <body className="bg-[radial-gradient(145.05%_100%_at_50%_0%,#00241d_0%,#00160f_57.38%,#222200_88.16%)] text-white">
        {children}
      </body>
    </html>
  );
}
