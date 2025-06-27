import GradientText from "../../src/pages/GradientText/GradientText";

export function Title() {
  return (
    <>
      <GradientText
        colors={["#02c6ff", "#0066ff", "#da00ff"]}
        animationSpeed={6}
        showBorder={false}
        className=" text-center text-6xl font-bold pt-2 min-w-full mb-6"
      >
        AI Readme Generator
      </GradientText>
      <div className="w-full max-w-xl text-center">
        <p className="text-white mb-14">
          Instantly create professional, well-structured README files for your
          GitHub projects using the power of AI.
        </p>
      </div>
    </>
  );
}
