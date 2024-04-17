import React from "react";

const Hero = () => {
  return (
    <div>
      <section className="hero">
        <div className="mx-auto sm:px-7 px-4 max-w-screen-xl">
          <div className="flex flex-col md:flex-row gap-20 items-center py-12">
            <div className="max-w-screenlg mx-auto text-center flex flex-col gap-5">
              <h1 className="font-black text-2xl md:text-5xl pts !leading-[34px] md:!leading-[60px]">
                Assistant{" "}
                <span className="bg-clip-text text-transparent bg-gradient-to-r from-yellow-300 to-green-500">
                  IA
                </span>{" "}
                qui résume
                <br />
                chaque jour les Actualités de la TVT.
              </h1>
            </div>
          </div>
        </div>
      </section>
    </div>
  );
};

export default Hero;
