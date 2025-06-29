import { motion } from "framer-motion";

const variants = {
  initial: { y: "-100%", position: "absolute" },
  animate: {
    y: "0%",
    position: "absolute",
    transition: { duration: 0.5, ease: "easeInOut" },
  },
  exit: {
    y: "100%",
    position: "absolute",
    transition: { duration: 0.5, ease: "easeInOut" },
  },
};

export default function SlidePageWrapperExit({ children }) {
  return (
    <motion.div
      className="w-full h-full"
      variants={variants}
      initial="initial"
      animate="animate"
      exit="exit"
    >
      {children}
    </motion.div>
  );
}
