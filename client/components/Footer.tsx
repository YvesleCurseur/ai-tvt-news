import React from "react";

const Footer = () => {
  return (
    <footer className="flex items-center px-4 py-10 mx-auto max-w-7xl">
      <p className="text-sm text-center text-gray-100 w-full">
        Fait par{" "}
        <a
          href="https://www.linkedin.com/in/fulbert-pognon/"
          className="hover:underline hover:text-white"
        >
          {" "}
          Fulbert Pognon{" "}
        </a>
      </p>
    </footer>
  );
};

export default Footer;
