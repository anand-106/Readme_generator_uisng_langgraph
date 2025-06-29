import { motion } from "framer-motion";

const variants = {
  initial: { position: "absolute", opacity: 0 },
  animate: {
    position: "absolute",
    transition: { duration: 0.3, ease: "easeOut" },
    opacity: 1,
  },
  exit: {
    position: "absolute",
    transition: { duration: 0.3, ease: "easeOut" },
    opacity: 0,
  },
};

export default function SlidePageWrapper({ children }) {
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
