import React from "react";

const Header = () => {
  return (
    <header>
      <div className="mx-auto sm:px-7 px-4 max-w-screen-xl pt-10 flex">
        <a href="/" className="text-xl text-white">
          AI TVT ACTUALITES CONCEPT
        </a>
        <nav className="ml-auto">
          <ul className="flex gap-10">
            <li>
              <a href="about" className="hover:underline hover:text-white">
                A PROPOS + DISCLAIMER
              </a>
            </li>
          </ul>
        </nav>
      </div>
    </header>
  );
};

export default Header;
